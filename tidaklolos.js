const params = new URLSearchParams(window.location.search);

const nisn = params.get("nisn");
const tanggal = params.get("tanggal");
const nama = params.get("nama");

console.log("Tanggal Lahir: ", tanggal);
console.log("Nama: ", nama);
console.log("NIR", nisn)

document.getElementById("nisn").textContent = nisn || "-"
document.getElementById("tanggal").textContent = tanggal || "-";
document.getElementById("nama").textContent = nama || "-";