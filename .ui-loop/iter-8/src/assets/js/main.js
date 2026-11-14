(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  document.documentElement.classList.add("js");
  if (!reduce) document.documentElement.classList.add("motion");

  var nav = document.getElementById("nav");
  var btn = nav && nav.querySelector(".menu");
  var main = document.getElementById("main");
  var bar = document.querySelector(".bar");
  function setNav(open) {
    if (!nav || !btn) return;
    nav.classList.toggle("open", open);
    document.body.classList.toggle("nav-open", open);
    btn.setAttribute("aria-expanded", open);
    btn.textContent = open ? "Close" : "Menu";
    if (main) {
      if (open) main.setAttribute("inert", "");
      else main.removeAttribute("inert");
    }
    if (bar) {
      if (open) bar.setAttribute("inert", "");
      else bar.removeAttribute("inert");
    }
  }
  if (btn) {
    btn.addEventListener("click", function () {
      setNav(!nav.classList.contains("open"));
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("open")) {
        setNav(false);
        btn.focus();
      }
      if (e.key !== "Tab" || !nav.classList.contains("open")) return;
      var items = nav.querySelectorAll("button, a[href]");
      if (!items.length) return;
      var first = items[0];
      var last = items[items.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    });
  }

  var header = document.querySelector(".top");
  var mosaic = document.querySelector(".mosaic");
  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      var doc = document.documentElement;
      var max = doc.scrollHeight - window.innerHeight;
      var p = max > 0 ? window.scrollY / max : 0;
      doc.style.setProperty("--scrolled", p.toFixed(4));
      if (header) header.classList.toggle("is-stuck", window.scrollY > 8);
      if (mosaic && !reduce) {
        var r = mosaic.getBoundingClientRect();
        var par = (window.innerHeight * 0.5 - (r.top + r.height * 0.5)) / window.innerHeight;
        mosaic.style.setProperty("--par", par.toFixed(3));
      }
      ticking = false;
    });
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  if (!reduce && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) e.target.classList.add("is-in");
      });
    }, { threshold: 0.18, rootMargin: "0px 0px -6% 0px" });
    document.querySelectorAll("main section, .uses, table.spec, .steps, .photos figure, .pack-shot, .who figure").forEach(function (el) {
      io.observe(el);
    });
  } else {
    document.querySelectorAll("main section, .uses, table.spec, .steps").forEach(function (el) {
      el.classList.add("is-in");
    });
  }

  if (!reduce) {
    document.addEventListener("click", function (e) {
      var a = e.target.closest('a[href^="#"]');
      if (!a || a.classList.contains("skip")) return;
      var id = a.getAttribute("href").slice(1);
      if (!id) return;
      var t = document.getElementById(id);
      if (!t) return;
      e.preventDefault();
      t.scrollIntoView({ behavior: "smooth", block: "start" });
      if (!t.hasAttribute("tabindex")) t.setAttribute("tabindex", "-1");
      t.focus({ preventScroll: true });
    });
  }

  var form = document.querySelector("form.enquiry");
  if (form) {
    var status = form.querySelector(".status");
    var submit = form.querySelector("button[type=submit]");
    var params = new URLSearchParams(window.location.search);
    var docs = params.get("need") === "docs" || params.get("intent") === "docs";
    var qty = form.querySelector("#quantity");
    var qtyLabel = document.querySelector('label[for="quantity"]');
    var qtyHint = qty && qty.parentElement && qty.parentElement.querySelector(".hint");
    var msgBox = form.querySelector("#message");
    var pageH = document.querySelector(".pagehead h1");
    var pageP = document.querySelector(".pagehead p");
    if (docs) {
      if (qty) qty.removeAttribute("required");
      if (qtyLabel) qtyLabel.textContent = "Quantity (MT)";
      if (qtyHint) qtyHint.textContent = "Optional when you only need documents";
      var fm = document.getElementById("fm");
      if (fm) fm.textContent = "Document request";
      if (msgBox && !msgBox.value) msgBox.value = "Please send the TDS, SDS and a sample CoA for LABSA 90%. No order yet.";
      if (submit) submit.textContent = "Send document request";
      if (pageH) pageH.textContent = "Request documents";
      if (pageP) pageP.textContent = "Ask for the TDS, SDS or a sample CoA for LABSA 90%. Quantity is optional if you are not placing an order.";
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      status.className = "status";
      if (form.website.value) return;
      ["name", "phone", "quantity", "consent"].forEach(function (id) {
        var el = form[id];
        if (el) { el.removeAttribute("aria-invalid"); el.removeAttribute("aria-describedby"); }
      });
      var firstBad = null;
      var msg = "Please add quantity in MT, your name and phone, and tick consent.";
      if (!form.name.value.trim()) { firstBad = form.name; msg = "Please add your name."; }
      else if (!form.phone.value.trim()) { firstBad = form.phone; msg = "Please add your phone number."; }
      else if (!docs && !form.quantity.value.trim()) { firstBad = form.quantity; msg = "Please add quantity in MT."; }
      else if (!form.consent.checked) { firstBad = form.consent; msg = "Please tick the consent box."; }
      if (firstBad) {
        status.id = status.id || "form-status";
        status.className = "status err";
        status.setAttribute("role", "alert");
        status.textContent = msg;
        firstBad.setAttribute("aria-invalid", "true");
        firstBad.setAttribute("aria-describedby", status.id);
        firstBad.focus();
        return;
      }
      var data = {};
      new FormData(form).forEach(function (v, k) { if (k !== "website") data[k] = v; });
      if (docs) data.intent = "docs";
      status.textContent = "Sending…";
      var idleLabel = submit ? submit.textContent : "";
      if (submit) {
        submit.disabled = true;
        submit.setAttribute("aria-busy", "true");
        submit.textContent = "Sending…";
      }
      fetch(form.dataset.endpoint, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(data) })
        .then(function (r) { if (!r.ok) throw new Error(r.status); form.reset(); status.textContent = "Thank you. Plant/sales will reply on +91 97277 02597 within one working day."; })
        .catch(function () {
          status.className = "status err";
          status.textContent = "We could not send the form. Please call +91 97277 02597, WhatsApp the same number, or email rkspl2019@gmail.com.";
        })
        .finally(function () {
          if (submit) {
            submit.disabled = false;
            submit.removeAttribute("aria-busy");
            submit.textContent = idleLabel || (docs ? "Send document request" : "Send quote request");
          }
        });
    });
  }
})();
