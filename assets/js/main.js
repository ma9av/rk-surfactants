(function () {
  var nav = document.getElementById("nav");
  var btn = nav && nav.querySelector(".menu");
  if (btn) {
    btn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      btn.setAttribute("aria-expanded", open);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("open")) {
        nav.classList.remove("open");
        btn.setAttribute("aria-expanded", "false");
        btn.focus();
      }
    });
  }

  var form = document.querySelector("form.enquiry");
  if (form) {
    var status = form.querySelector(".status");
    var submit = form.querySelector("button[type=submit]");
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
      else if (!form.quantity.value.trim()) { firstBad = form.quantity; msg = "Please add quantity in MT."; }
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
      status.textContent = "Sending…";
      if (submit) { submit.disabled = true; submit.setAttribute("aria-busy", "true"); }
      fetch(form.dataset.endpoint, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(data) })
        .then(function (r) { if (!r.ok) throw new Error(r.status); form.reset(); status.textContent = "Thank you. Plant/sales will reply on +91 97277 02597 within one working day."; })
        .catch(function () {
          status.className = "status err";
          status.textContent = "We could not send the form. Please call +91 97277 02597, WhatsApp the same number, or email rkspl2019@gmail.com.";
        })
        .finally(function () {
          if (submit) { submit.disabled = false; submit.removeAttribute("aria-busy"); }
        });
    });
  }
})();
