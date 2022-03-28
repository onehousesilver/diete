import Swiper from "swiper";

export default function swiper() {
  new Swiper(".swiper-container", {
    loop: true,
    slidesPerView: 4,
    spaceBetween: 20,
    navigation: {
      prevEl: ".swiper-prev",
      nextEl: ".swiper-next",
    },
  });
}
