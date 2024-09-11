Syauqi Muhammad Yasman\
2306275752\
PBP D

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
![image](https://github.com/user-attachments/assets/8a0853b0-0018-4088-be57-54d16b5a9a10)
Pengguna dengan web browser akan meminta sebuah request melalui urls.py, kemudian urls.py akan memenuhi permintaan pengguna, apakah pengguna hanya meminta views atau juga dengan model, jika pengguna juga meminta model, maka models.py akan mengambilkan data yang berada di database. Kemudian data tersebut ditampilkan pada oleh views.py ke dalam berkas html.

### Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git berfungsi sebagai version control. Di mana git bekerja untuk menyimpan seluruh perubahan yang terjadi ketika kita sedang mengembangkan sebuah perangkat lunak. Dengan menggunakan git, kita dapat melakukan rollback jika terjadi sebuah kesalahan besar di tengah pengembangan perangkat lunak dengan mudah, karena versi-versi sebelumnya telah disimpan oleh git.

### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Karena Django menggunakan bahasa pemrograman Python sebagaimana yang kita pelajari pada mata kuliah Dasar-dasar Pemrograman 1. Selain itu, Django juga memiliki komunitas yang besar, sehingga tersedia banyak dukungan yang beredar di internet terkait masalah-masalah yang sering terjadi khususnya bagi seorang permula.

### Mengapa model pada Django disebut sebagai ORM?
Django disebut sebagai ORM karena memungkinkan developer untuk memetakan objek Python ke dalam tabel-tabel di database relasional, sehingga interaksi dengan database dapat dilakukan tanpa menulis query SQL secara langsung.
