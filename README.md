Link Deployment:http://zufar-romli-arlicgoodshop.pbp.cs.ui.ac.id

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab: 
- Membuat repositori GitHub baru bernama arlicshop dengan visibilitas public
- inisiasi direktori lokal arlicshop sebagai repositori git 
- menambahkan berkas gitignore
- Melakukan add, commit, dan push dari direktori lokal
- Menjalankan perintah django-admin startproject mental_health_tracker . untuk membuat direktori proyek arlicshop
- Melakukan persiapan awal dengan mengaktifkan virtual environment dengan menjalankan perintah env\Scripts\activate
- Membuat aplikasi main dalam proyek arlicshop
- menjalankan perintah "python manage.py startapp main" untuk membuat aplikasi baru dengan nama main
- Mendaftarkan aplikasi main ke dalam proyek
- Buka berkas settings.py di dalam direktori proyek arlicshop
- Tambahkan main ke dalam daftar aplikasi sebagai elemen terakhir yang dapat diakses pada variabel INSTALLED_APPS
- Membuat template
- Membuat dan mengisi berkas main.html
- Buat direktori baru bernama templates di dalam direktori aplikasi main.
- Buat main.html di dalam direktori templates.
- Isi main.html dengan menampilkan nama e-commerce, nama saya, dan kelas pbp saya
- Mencoba membuka berkas main.html di peramban web
- Implementasi model
- Buka berkas models.py
- isi berkas models.py dengan suatu class dengan nama Product dan isi class attribute, yaitu name, price, description. name sebagai nama item dengan tipe CharField, price sebagai harga item dengan tipe IntegerField, dan description sebagai deskripsi item dengan tipe TextField.
- Membuat dan mengaplikasikan migrasi model
- Menjalankan perintah python manage.py makemigrations untuk membuat migrasi model
- Menjalankan perintah python manage.py migrate untuk migrasi ke dalam basis data lokal
- Menghubungkan view dengan template
- mengintegrasikan komponen MVT
- Buka berkas views.py yang ada pada aplikasi main
- tambahkan baris import, yaitu from django.shortcuts import render
- tambahkan fungsi show_main di bawah impor yang berisi data yang disertakan pada main.html, yaitu nama dan kelas saya.
- Memodifikasi main.html dan ubah nama serta kelas menjadi struktur django yang sesuai untuk menampilkan data.
- Mengonfigurasi Routing URL
- Buat berkas urls.py di dalam direktori main
- isi berkas tersebut dengan impor path dari django.urls dan import show_main dari main.views. Lalu, deklarasi variabel app_name dengan 'main' dan buat variabel urlpatterns yang merupakan list yang menyimpan path dari django.urls.
- Buka berkas urls.py di dalam direktori proyek arlic_shop
- Impor fungsi include dari django.urls
- Tambahkan rute URL seperti berikut untuk mengarahkan tampilan main di dalam variabel urlpatterns.
    urlpatterns = [
        ...
        path('', include('main.urls')),
        ...
    ]
- Mencoba menjalankan proyek django dengan perintah python manage.py runserver
- Mencoba membuka http://localhost:8000/ untuk melihat halaman yang sudah dibuat
- Mengakses PWS untuk deployment
- Membuat proyek baru dengan nama arlic-shop
- Menyimpan informasi project credential dan project command.
- Pada settings.py, tambahkan url deployment pada ALLOWED_HOSTS.
- Jalankan git add, commit, dan push perubahan ke repo GitHub.
- Jalankan perintah project command pada halaman PWS.
- Cek situs PWS, dan lihat perkembangan proyek. Apabila sudah berhasil, cek proyek dengan view project.
- Apabila halaman sudah sesuai, proyek berhasil di-deploy


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jawab: 
Bagan: https://www.figma.com/design/IzhazAo84YbHat8EjPMWEx/Untitled?node-id=0-1&t=7gfYgaVLnW6M8nZS-1
Penjelasan: Model berfungsi untuk menyimpan data dan logika aplikasi. View berfungsi untuk menampilkan data dari model dan menghubungkannya dengan template. Template berfungsi untuk menentukan tampilan antarmuka pengguna. Pertama, client akan request terlebih dahulu. Lalu, urls.py akan berfungsi untuk menentukan rute atau url mana yang akan menangani request client tersebut. URL dipetakan ke views.py yang berfungsi untuk menangani logic dari request tersebut. Views.py juga akan menggunakan model jika diperlukan dan menentukan respons yang akan dikirim ke client serta mengambil data dari models.py karena models.py berfungsi untuk mendefinisikan struktur data dalam aplikasi Django yang memungkinkan interaksi antara aplikasi dan database menggunakan ORM. Lalu, template HTML diisi dengan data yang telah diproses oleh views.py dan hasilnya dikirimkan kembali ke client.

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Jawab: Git memiliki fungsi yang cukup krusial dalam pengembangan perangkat lunak. Para pengembang perangkat lunak dapat berkolaborasi dalam mengembangkan proyek dan memastikan integritas kode. Berikut setidaknya tiga fungsi git dalam pengembangan perangkat lunak. Pertama, version control, yaitu untuk melacak setiap perubahan pada sumber kode. Git dapat mencatat setiap perubahan dan dapat secara fleksibel kembali ke versi sebelumnya jika diperlukan. Kedua, kolaborasi, yaitu git memungkinkan untuk banyak pengembang dalam mengembangkan sautu proyek secara bersamaan. Masing-masing pengembang akan bekerja di branch terpisah dan akan di merge apabila sudah siap. Ketiga, git dapat menyimpan data penting yang pernah dilakukan pada proyek sehingga memungkinkan pengembang untuk mengeksperimen, mencoba hal baru, tanpa takut terjadi kesalahan atau masalah.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Jawab: Framework django dijadikan permulaan pembelajaran perangkat lunak karena beberapa hal. Pertama, open source, yaitu framework yang tersedia secara gratis sehingga cocok untuk permulaan dalam pembelajaran. Kedua, Django sangat cepat dan efisien dalam mengembangkan fitur-fitur penting tanpa harus mulai dari nol. Ketiga, Django memiliki fitur bawaan yang sangat lengkap mencakup sistem autentikasi pengguna, manajemen database menggunakan ORM, dan lain sebagainya. Keempat, Django sangat fokus pada keamanan. Django dapat melindungi aplikasi dari keamanan umum sehingga para pengembang pemula tidak perlu khawatir terkait keamanan. Kelima, Django dirancang untuk skala besar sehingga dalam permulaan pembelajaran sangat penting untuk mengenal iklim kerja dengan skala besar. Keenam, Django multifungsi atau pun serbaguna dengan dapat digunakan untuk berbagai jenis proyek.

5. Mengapa model pada Django disebut sebagai ORM?
Jawab: Model pada Django disebut sebagai ORM karena objek dipetakan pada kode python ke tabel dalam database relasional. Teknik ORM merupakan teknik pemrograman yang menghubungkan elemen-elemen dalam pemrograman berbasis objek dengan elemen-elemen di dalam database relasional.
