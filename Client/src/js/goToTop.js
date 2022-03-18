/* eslint-disable */
import gsap from "gsap";
import _ from "lodash";

export default function scroll() {
  const toTopEl = document.querySelector("#to-top");
  window.addEventListener(
    "scroll",
    _.throttle(function () {
      if (window.scrollY > 300) {
        gsap.to(toTopEl, 0.2, {
          x: 0,
        });
      } else {
        gsap.to(toTopEl, 0.2, {
          x: 100,
        });
      }
    }, 200)
  );


  const spyEls = document.querySelectorAll("section .scroll-spy");
  
  spyEls.forEach(function (spyEl) {
    new ScrollMagic.Scene({
      triggerElement: spyEl, //보여짐 여부를 감시할 요소를 triggerElment에 지정
      triggerHook: 0.8,
    })
      .setClassToggle(spyEl, "show")
      .addTo(new ScrollMagic.Controller());
  });
}
