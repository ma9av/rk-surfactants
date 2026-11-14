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
  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      var doc = document.documentElement;
      var max = doc.scrollHeight - window.innerHeight;
      var p = max > 0 ? window.scrollY / max : 0;
      if (!reduce) doc.style.setProperty("--scrolled", p.toFixed(4));
      if (header) header.classList.toggle("is-stuck", window.scrollY > 8);
      ticking = false;
    });
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  var reel = document.querySelector(".reel");
  if (reel) {
    var slides = reel.querySelectorAll(".reel-slide");
    var steps = reel.querySelectorAll(".reel-steps button");
    var track = reel.querySelector(".reel-track");
    var playBtn = reel.querySelector(".reel-play");
    var cur = 0;
    var leaving = null;
    var leaveTimer;
    var pending = null;

    function sync() {
      slides.forEach(function (s, i) {
        var on = i === cur;
        s.toggleAttribute("inert", !on);
        if (on) s.removeAttribute("aria-hidden"); else s.setAttribute("aria-hidden", "true");
      });
      steps.forEach(function (b, i) {
        if (i === cur) b.setAttribute("aria-current", "true"); else b.removeAttribute("aria-current");
      });
    }

    function show(n, back) {
      n = (n + slides.length) % slides.length;
      if (n === cur) return;
      var prev = slides[cur];
      if (leaving) leaving.classList.remove("is-leaving");
      reel.classList.toggle("is-back", !!back);
      void getComputedStyle(slides[n]).clipPath;
      prev.classList.remove("is-active");
      prev.classList.add("is-leaving");
      leaving = prev;
      var next = slides[n];
      next.classList.add("is-active");
      cur = n;
      sync();
      if (pending) pending.el.removeEventListener("transitionend", pending.fn);
      clearTimeout(leaveTimer);
      function done(e) {
        if (e && (e.target !== next || e.propertyName !== "clip-path")) return;
        next.removeEventListener("transitionend", done);
        clearTimeout(leaveTimer);
        pending = null;
        prev.classList.remove("is-leaving");
        if (leaving === prev) leaving = null;
      }
      if (reduce) { done(); return; }
      pending = { el: next, fn: done };
      next.addEventListener("transitionend", done);
      leaveTimer = setTimeout(done, 2000);
    }

    function setStopped(stop) {
      reel.classList.toggle("is-stopped", stop);
      track.setAttribute("aria-live", stop ? "polite" : "off");
      playBtn.setAttribute("aria-label", stop ? "Start slide rotation" : "Pause slide rotation");
    }

    reel.querySelector(".reel-next").addEventListener("click", function () { show(cur + 1); });
    reel.querySelector(".reel-prev").addEventListener("click", function () { show(cur - 1, true); });
    playBtn.addEventListener("click", function () { setStopped(!reel.classList.contains("is-stopped")); });
    steps.forEach(function (b, i) {
      b.addEventListener("click", function () { show(i, i < cur); });
    });
    reel.querySelector(".reel-steps").addEventListener("animationend", function (e) {
      if (e.animationName === "reel-fill") show(cur + 1);
    });

    reel.addEventListener("mouseenter", function () { reel.classList.add("is-held"); });
    reel.addEventListener("mouseleave", function () {
      if (!reel.querySelector(":focus-visible")) reel.classList.remove("is-held");
    });
    reel.addEventListener("focusin", function (e) {
      if (e.target.matches(":focus-visible")) reel.classList.add("is-held");
    });
    reel.addEventListener("focusout", function (e) {
      if (!reel.contains(e.relatedTarget) && !reel.matches(":hover")) reel.classList.remove("is-held");
    });
    reel.addEventListener("keydown", function (e) {
      if (e.key === "ArrowRight") { e.preventDefault(); show(cur + 1); }
      else if (e.key === "ArrowLeft") { e.preventDefault(); show(cur - 1, true); }
    });

    var frame = reel.querySelector(".reel-frame");
    var startX = null;
    frame.addEventListener("pointerdown", function (e) { startX = e.clientX; });
    frame.addEventListener("pointerup", function (e) {
      if (startX === null) return;
      var dx = e.clientX - startX;
      startX = null;
      if (Math.abs(dx) > 40) show(dx < 0 ? cur + 1 : cur - 1, dx > 0);
    });
    frame.addEventListener("pointercancel", function () { startX = null; });

    setStopped(reduce);
    sync();
  }

  if (!reduce && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) e.target.classList.add("is-in");
      });
    }, { threshold: 0.18, rootMargin: "0px 0px -6% 0px" });
    document.querySelectorAll("main section, .uses, table.spec, .steps, .ph").forEach(function (el) {
      io.observe(el);
    });
  } else {
    document.querySelectorAll("main section, .uses, table.spec, .steps, .ph").forEach(function (el) {
      el.classList.add("is-in");
    });
  }

  if (!reduce) {
    document.addEventListener("click", function (e) {
      var a = e.target.closest('a[href^="#"]');
      if (!a) return;
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
      var docsLink = form.querySelector('a[href*="need=docs"]');
      if (docsLink) {
        var wrap = docsLink.closest(".docs") || docsLink;
        wrap.hidden = true;
      }
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      status.className = "status";
      if (form.website.value) return;
      ["name", "phone", "quantity"].forEach(function (id) {
        var el = form[id];
        if (el) { el.removeAttribute("aria-invalid"); el.removeAttribute("aria-describedby"); }
      });
      var firstBad = null;
      var msg = "Please add quantity in MT, your name and phone.";
      if (!form.name.value.trim()) { firstBad = form.name; msg = "Please add your name."; }
      else if (!form.phone.value.trim()) { firstBad = form.phone; msg = "Please add your phone number."; }
      else if (!docs && !form.quantity.value.trim()) { firstBad = form.quantity; msg = "Please add quantity in MT."; }
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
