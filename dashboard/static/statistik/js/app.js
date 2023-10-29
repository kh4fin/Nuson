const btnHapus = document.querySelectorAll(".hapus-link"); // Menggunakan class "hapus-link" yang sesuai dengan tag <a> di HTML
const apiUrl = "http://127.0.0.1:8000/api/nuson/";

btnHapus.forEach((link) => {
  link.addEventListener("click", (event) => {
    event.preventDefault(); // Mencegah tindakan bawaan dari tag <a> (navigasi ke URL)

    if (confirm("Apakah Anda yakin ingin menghapus data ini?")) {
      const dataId = link.getAttribute("data-id"); // Mendapatkan data-id dari atribut data-id

      fetch(`${apiUrl}${dataId}/`, {
        method: "DELETE",
      })
        .then((response) => {
          if (response.status === 204) {
            alert("Data berhasil dihapus.");
            location.reload(); // Memuat ulang halaman setelah penghapusan
          } else {
            alert("Gagal menghapus data.");
          }
        })
        .catch((error) => {
          console.error("Terjadi kesalahan:", error);
          alert("Gagal menghapus data.");
        });
    }
  });
});
