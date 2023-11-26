# Algeo02-22135

<h2 align="center">
  HTML Checker dengan pushdown automata <br/>
</h2>
<hr>

## Table of Contents

- [Deskripsi Permasalahan](#Deksripsi-Permasalahan)
- [Anggota Kelompok](#Anggota-Kelompok)
- [Cara Menggunakan](#Cara-Menggunakan)
- [Project Status](#project-status)

## Deskripsi Permasalahan

HTML (Hypertext Markup Language) adalah bahasa markup yang digunakan untuk membuat struktur dan tampilan konten web. HTML adalah salah satu bahasa utama yang digunakan dalam pengembangan web dan digunakan untuk menggambarkan bagaimana elemen-elemen konten, seperti teks, gambar, tautan, dan media, akan ditampilkan di browser web. Setiap dokumen HTML dimulai dengan elemen html, lalu diikuti dengan head (untuk metadata dan tautan ke file eksternal) dan body (untuk konten yang akan ditampilkan)

HTML menggunakan elemen-elemen (tags) untuk mengelompokkan dan mengatur konten. Contohnya adalah atribut src untuk gambar, href untuk tautan, dan class untuk memberikan elemen kelas CSS.

Sama seperti bahasa pada umumnya, HTML juga memiliki sintaks tersendiri dalam penulisannya yang dapat menimbulkan error jika tidak dipenuhi. Meskipun web browser modern seperti Chrome dan Firefox cenderung tidak menghiraukan error pada HTML memastikan bahwa HTML benar dan terbentuk dengan baik masih penting untuk beberapa alasan seperti Search Engine Optimization (SEO), aksesibilitas, maintenance yang lebih baik, kecepatan render, dan profesionalisme.

Dibutuhkan sebuah program pendeteksi error untuk HTML. Oleh sebab itu, implementasikan sebuah program yang dapat memeriksa kebenaran HTML dari segi nama tag yang digunakan serta attribute yang dimilikinya. Pada tugas pemrograman ini, gunakanlah konsep Pushdown Automata (PDA) dalam mencapai hal tersebut yang diimplementasikan dalam bahasa Python.

## Anggota Kelompok

| NIM      | Nama                       |
| -------- | -------------------------- |
| 13522135 | Christian Justin Hendrawan |
| 13522145 | Farrel Natha Saskoro       |
| 13522156 | Jason Fernando             |

## Cara Menggunakan

1. Buka folder projek ini pada terminal lalu ketik command berikut:

```shell
cd src
```

2. Setelah itu, masukkan command

```shell
python main.py pda.txt "<Nama file yang ingin dites>"
```

## Project Status

Project is: _complete_
