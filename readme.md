Syauqi Muhammad Yasman\
2306275752\
PBP D

## Tugas 2
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat repository di github kemudian clone repository tersebut
2. Mengaktifkan virtual environment
3. Menginstall Django dan requirements lainnya
4. Membuat proyek dan menambah izinkan localhost
5. Membuat aplikasi main
6. Membuat model dan migrasi
7. Mengonfigurasi view dan url
8. Membuat template
### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Bagan request klien Django](https://github.com/user-attachments/assets/8a0853b0-0018-4088-be57-54d16b5a9a10)
Pengguna dengan web browser akan meminta sebuah request melalui urls.py, kemudian urls.py akan memenuhi permintaan pengguna, apakah pengguna hanya meminta views atau juga dengan model, jika pengguna juga meminta model, maka models.py akan mengambilkan data yang berada di database. Kemudian data tersebut ditampilkan pada oleh views.py ke dalam berkas html.

### Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git berfungsi sebagai version control. Di mana git bekerja untuk menyimpan seluruh perubahan yang terjadi ketika kita sedang mengembangkan sebuah perangkat lunak. Dengan menggunakan git, kita dapat melakukan rollback jika terjadi sebuah kesalahan besar di tengah pengembangan perangkat lunak dengan mudah, karena versi-versi sebelumnya telah disimpan oleh git.

### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Karena Django menggunakan bahasa pemrograman Python sebagaimana yang kita pelajari pada mata kuliah Dasar-dasar Pemrograman 1. Selain itu, Django juga memiliki komunitas yang besar, sehingga tersedia banyak dukungan yang beredar di internet terkait masalah-masalah yang sering terjadi khususnya bagi seorang permula.

### Mengapa model pada Django disebut sebagai ORM?
Django disebut sebagai ORM karena memungkinkan developer untuk memetakan objek Python ke dalam tabel-tabel di database relasional, sehingga interaksi dengan database dapat dilakukan tanpa menulis query SQL secara langsung.

## Tugas 3

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery dibutuhkan untuk pengiriman sebuah data baik dari klien ke server maupun server ke klien. Dengan implementasi data delivery pada sebuah web platform, kita dapat membuat interaksi dua arah dari klien ke server dan sebaliknya. Contohnya adalah klien menambahkan sebuah produk ke server dan server menampilkan produk-produk yang tersedia ke klien.
### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Keduanya memiliki kelebihan dan kekurangannya masing-masing, JSON memiliki keterbatasan tipe data dibandingkan dengan XML, XML mendukung tipe data binary dan timestamp sementara JSON tidak. Namun, JSON memiliki strukturnya yang lebih mudah dipahami dan memiliki waktu parsing lebih cepat daripada XML. Dari keterbatasan tipe data yang didukung oleh JSON, dan mungkin jarang digunakan, dibandingkan dengan struktur yang simpel dan kecepatannya, menjadikan JSON lebih mudah digunakan dalam pengembangan ketimbang XML, sehingga membuatnya dapat lebih populer.
### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi method tersebut adalah untuk memverifikasi apakah input yang diisi oleh pengguna sesuai dengan apa yang telah kita rancang pada model. Hal tersebut dilakukan untuk mencegah terjadinya error karena perbedaan tipe data.
### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
CRSF Token merupakan token random yang sulit ditebak dan digunakan untuk memverifikasi apakah sebuah tindakan yang dilakukan berasal benar-benar dari pengguna. Tanpa adanya CRSF Token, penyerang dapat membuat request tanpa persetujuan pengguna ke sebuah website yang memiliki kerentanan CRSF. Hal tersebut dapat dilakukan penyerang melalui website berbahaya yang berusaha mengirimkan request ke suatu website yang sedang menjalankan session kita.

Tanpa token:
```
http://www.mybank.com/transfer?to=123456&amount=10000
```
Dengan token:
```
http://www.mybank.com/transfer?to=123456&amount=10000&token=31415926535897932384626433832795028841971
```
Dengan token CRSF, penyerang tidak bisa menebak token tersebut, sehingga request yang dikirimkan penyerang ditolak.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). 
1. Membuat base.html
2. Menambahkan base.html template ke settings
3. Membuat main.html melakukan extend terhadap base.html
4. Menambahkan uuid ke model sebagai key
5. Menjalankan migrasi baru
6. Membuat form input
7. Menampilkan data di main
8. Membuat pengembalian data xml dan json

### Postman
#### XML
![Postman XML](https://github.com/user-attachments/assets/6c8404a7-5a15-4f2f-b12f-fa151e226784)
#### XML/id
![Postman XML with id](https://github.com/user-attachments/assets/c84eb116-dee2-48b2-8a16-448c8f3236dc)
#### JSON
![Postman JSON](https://github.com/user-attachments/assets/dc0c4212-e619-478c-b6c4-4249e647195f)
#### JSON/id
![Postman JSON with id](https://github.com/user-attachments/assets/b68875e1-e52f-4767-993c-1dc63ffef844)