document.body.style.backgroundImage = "url('/assets/frame_52.png')";
document.body.style.backgroundRepeat = "no-repeat";
document.body.style.backgroundSize = "auto";
document.body.style.backgroundPosition = "center right";

function collapseActiveSectionIndexNav() {
  const normalize = (href) => {
    try {
      const url = new URL(href, window.location.origin);
      return url.pathname.replace(/\/index\.html$/, "/").replace(/\/$/, "");
    } catch (_) {
      return "";
    }
  };

  const current = normalize(window.location.href);
  document.querySelectorAll(".md-nav__container > a.md-nav__link--active[href]").forEach((link) => {
    if (normalize(link.href) !== current) return;
    const container = link.closest(".md-nav__container");
    const sectionItem = container && container.closest(".md-nav__item");
    const childNav = sectionItem && sectionItem.querySelector(":scope > .md-nav");
    if (!childNav) return;

    childNav.querySelectorAll(":scope > .md-nav__list > .md-nav__item > .md-nav__toggle").forEach((toggle) => {
      if (!toggle.checked) return;
      toggle.checked = false;
      const nested = toggle.closest(".md-nav__item")?.querySelector(":scope > .md-nav");
      if (nested) nested.setAttribute("aria-expanded", "false");
    });
  });
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", collapseActiveSectionIndexNav);
} else {
  collapseActiveSectionIndexNav();
}

(function(){if(!window.chatbase||window.chatbase("getState")!=="initialized"){window.chatbase=(...arguments)=>{if(!window.chatbase.q){window.chatbase.q=[]}window.chatbase.q.push(arguments)};window.chatbase=new Proxy(window.chatbase,{get(target,prop){if(prop==="q"){return target.q}return(...args)=>target(prop,...args)}})}const onLoad=function(){const script=document.createElement("script");script.src="https://www.chatbase.co/embed.min.js";script.id="zxB2uzZfYoHIpA98eTzgM";script.domain="www.chatbase.co";document.body.appendChild(script)};if(document.readyState==="complete"){onLoad()}else{window.addEventListener("load",onLoad)}})();
