
import gsap from "gsap";
import _ from "lodash";
import ScrollMagic from "scrollmagic";

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

  const scrollEl = document.querySelector('.scroll-container');
  window.addEventListener(
    "scroll",
    _.throttle(function () {
      if (window.scrollY > 200) {
        gsap.to(scrollEl, 0.2, {
          opacity: 0,
        });
      } else {
        gsap.to(scrollEl, 0.2, {
          opacity: 1,
        });
      }
    }, 200)
  )
  const spyEls = document.querySelectorAll("section.scroll-spy");
  // 요소들 반복 처리!
  spyEls.forEach(function (spyEl) {
    new ScrollMagic.Scene({
      // 감시할 장면(Scene)을 추가
      triggerElement: spyEl, // 보여짐 여부를 감시할 요소를 지정
      triggerHook: 0.8, // 화면의 80% 지점에서 보여짐 여부 감시
    })
      .setClassToggle(spyEl, "show") // 요소가 화면에 보이면 show 클래스 추가
      .addTo(new ScrollMagic.Controller()); // 컨트롤러에 장면을 할당(필수!)
  });
}
