Link Deployment:http://zufar-romli-arlicgoodshop.pbp.cs.ui.ac.id

Tugas 2
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

Tugas 3

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Jawab: Data delivery penting dalam pengimplementasian sebuah platform karena beberapa hal. Pertama, keamanan data. Data delivery akan melibatkan keamanan yang baik dengan mengenkripsi data selama pengiriman. Hal ini penting untuk menghindari serangan siber. Kedua, kecepatan dan performa. Dalam platform yang besar, kecepatan pengiriman data sangat penting agar platform bisa beroperasi lebih cepat dan responsif. Ketiga, skalabilitas yang besar. Platform yang berkembang pesat akan merasakan bertambahnya pengguna sehingga sistem data delivery harus mampu mengimbangi permintaan yang meningkat.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Jawab: JSON dianggap lebih baik dibanding JSON, sekaligus lebih populer. JSON dianggap lebih populer dibandingkan XML karena beberapa hal. Pertama, sintaks yang sederhana dan ringkas. Bagi para programmer, terutama programmer pemula, sintaks menjadi hal krusial dalam perjalanan membangun sebuah proyek. Sintaks yang sederhana dan ringkas dapat dengan mudah diproses oleh mesin, sedangkan XML memiliki tag pembuka dan penutup yang memperbesar ukuran file. Kedua, parsing lebih cepat dan mudah. JSON lebih cepat untuk di-parse di kebanyakan bahasa pemrograman sehingga mendukung JSON untuk parsing data secara efisien, sedangkan XML biasanya membutuhkan tools tambahan yang lebih kompleks dan lambat. Ketiga, JSON dirancang untuk penyajian data secara langsung sehingga sangat cocok untuk digunakan dalam menyimpan data sederhana, sedangkan XML lebih cocok mendukung elemen-elemen lain, seperti atribut, namespace, dan dokumen lainnya yang lebih terstruktur. Hal tersebut dirasa kurang efektif apabila hanya digunakan untuk pertukaran data.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Jawav: Fungsi dari method is_valid() pada form Django adalah untuk memastikan form berisi data yang valid sesuai dengan aturan yang telah didefinisikan, memicu validasi field, serta mengakses data bersih. Alasan kita membutuhkan method tersebut adalah untuk mempermudah pengolahan data, memastikan keamanan input, serta penanganan kesalahan yang terpusat.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Jawab: Kita membutuhkan csrf_token saat membuat form di Django karena csrf_token merupakan salah satu mekanisme keamanan utama yang digunakan oleh Django untuk melindungi aplikasi dari serangan CSRF. Jika kita tidak menambahkan crsf_token pada form Django, akan ada penyalahgunaan hak akses serta pengguna dapat terjebak untuk mengirimkan permintaan yang tidak valid. Hal tersebut dapat dimanfaatkan oleh penyerang dengan mengirimkan permintaan melalui situs eksternal. Biasanya para pengguna tidak menyadari bahwa mereka telah menjawab permintaan yang tidak sah yang dilakukan oleh penyerang. Contohnya adalah penipuan uang yang dilakukan melalui situs web eksternal. Hal tersebut tentunya dapat merugikan pengguna. 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab: 
- Membuat direktori templates pada direktori utama. Lalu, buat berkas HTML baru bernama base.html.
- Buka settings.py pada direktori arlicgoodshop. Lalu, pada variabel TEMPLATES, sesuaikan kode yang ada agar base.html dapat terdeteksi sebagai berkas template.
- Mengubah kode berkas main.html pada subdirektori templates yang ada pada direktori main.
- Menghapus db.sqlite3
- Import uuid
- tambahkan variabel id yang isinya adalah models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
- Melakukan migrasi model
- Membuat forms.py pada direktori main
- Isi forms.py dengan kode yang tujuannya sebagai struktur form yang dapat menerima data shop entry
- Buka views.py dan tambahkan beberapa import
- Buat fungsi create_item_entry dengan parameter request pada views.py
- Masukkan 'mood_entries': mood_entries pada fungsi show_main
- Buka urls.py pada direktori main dan impor fungsi create_item_entry
- Tambahkan path pada url patterns untuk mengakses fungsi yang sudah diimpor sebelumnya
- Buat berkas HTML baru dengan nama create_item_entry.html pada direktori main/templates
- Buka main.html dan tambahkan kode yang akan menampilkan data mood dalam bentu tabel
- Buka views.py pada direktori main dan import HttpResponse dan Serializer
- Tambahkan fungsi show_xml, show_json, show_xml_by_id, dan show_json_by_id yang mengembalikan response dari requester.
- Buka urls.py pada direktori main dan impor fungsi yang sudah dibuat barusan
- Tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi
- Menggunakakan postman untuk melihat data yang telah masuk
- Melakukan push pws secara otomatis menggunakan GitHub Actions.

### Screenshot Postman 
- JSON
![json](https://github.com/user-attachments/assets/4aa1d2d8-9bc1-4df9-94f6-7336e9837772)
- JSON BY ID
![json id](https://github.com/user-attachments/assets/1377c939-9ee3-471e-8d1a-e47ec44642b1)
- XML
![xml](https://github.com/user-attachments/assets/2aa3bb29-ee5a-4605-aaee-090f2cdbbe34)
- XML BY ID
![xml id](https://github.com/user-attachments/assets/9e9627ab-a0e8-4615-8365-fe3e26913e67)


Tugas 4
1. Apa perbedaan antara HttpResponseRedirect() dan redirect()?
Jawab: Terdapat beberapa perbedaan antara kedua fungsi tersebut. Pertama, HttpResponseRedirect() memerlukan URL lengkap, sementara redirect() dapat menerima URL, URL lengkap, atau path relatif. Kedua, HttpResponseRedirect() diimpor dari django.http, sementara redirect() diimpor dari django.shortcuts. Ketiga, HttpResponseRedirect() adalah kelas tingkat rendah, sementara redirect() adalah fungsi tingkat tinggi yang memanggil HttpResponseRedirect(). Dari segi penggunaan, redirect() cenderung lebih mudah untuk digunakan.

2. Jelaskan cara kerja penghubungan model Product dengan User!
Jawab: Penghubungan model Product dengan User bertujuan agar para User dapat melihat ItemEntriesnya yang dibuatnya sendiri, tanpa melihat punya User lain. Pertama, kita perlu hubungkan salah satu model yang kita gunakan dengan satu user melalui suatu relationship. Relationship adalah suatu hubungan yang terasosiasikan antara dua entitas. Dalam hal ini, dua entitas tersebut adalah item entry dan user. Lalu, pada views kita buat suatu conditional agar Django tidak langsung menyimpan objek yang telah dibuat dari form langsung ke database. Hal tersebut agar kita dapat memodifikasi objek tersebut dengan menandakan objek tersebut dimiliki oleh pengguna yang sedang login. Kemudian, pada fungsi show_main pada views.py, kita dapat assign variabel item_entries dengan ItemEntry.objects.filter(user=request.user). Hal tersebut bertujuan agar objek ItemEntry dapat terasosiasikan dengan User yang sedang login. Selain itu, kita dapat menampilkan nama user yang sedang login pada tampilan dengan mengisi key, value pada dictionary context dengan 'nama' : request.user.username. Terakhir, setelah melakukan semua perubahan, lakukan migrasi model dengan command python manage.py makemigrations yang dilanjutkan dengan command python manage.py migrate. Coba jalankan proyek dan seharusnya model telah terasosiasikan dengan User.

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Jawab: Authentication adalah suatu mekanisme verifikasi identitas User, sementara authorization adalah mekanisme menentukan apa yang boleh dilakukan oleh User yang telah terautentikasi. Pada saat User login, sistem akan melakukan mekanisme autentikasi terlebih dahulu untuk memverifikasi data User. Kemudian, jika autentikasi berhasil, sistem dapat menetapkan autorisasi berdasarkan identitas User tersebut. Pada authentication, Django menggunakan sistem autentikasi bawaan yang ada di django.contrib.auth. Terdapat beberapa implementasi dari autentikasi oleh django, yaitu django menyediakan model User bawaan, menyediakan login form bawaan, serta menyediakan view login, logout, dan perubahan passsword. Untuk authorization, django menggunakan sistem permission dan group untuk otorisasi. Terdapat beberapa implementasi dari otorisasi oleh django, yaitu django secara otomatis membuat permissions untuk setiap model, memungkinkan pengelompokan Users dengan permissions yang sama, dan menyediakan decorator, seperti @login_required.

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Jawab: Terdapat beberapa cara agar django dapast mengingat pengguna yang telah login. Pertama, sessions. Django membuat sebuah session di server yang mana session menyimpan informasi User, termasuk men-generate session ID yang unik untuk setiap sessions. Kedua, cookies. sessions ID yang telah digenerate oleh sessions, disimpan pada cookie di browser User. Setiap User membuat request, cookie akan dikirim ke server. Ketiga, proses autentikasi yang mana server menerima cookie session id dan mengambil data session dari server. Kegunaan lain dari cookies adalah untuk menyimpan pengaturan tampilan, menganalisis perilaku User, menyimpan token autentikasi, dan lain-lain. Tidak semua cookies aman digunakan, seperti HttpOnly Flag yang mana cookies tersebut tidak dapat diakses oleh JavaScript. Cookies hanya dapat dikirim melalui koneksi Https. Sebaiknya, simpan data yang benar-benar diperlukan dalam cookies dan data sensitif sebaiknya dienkripsi.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab:

a. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
step by step: 
- Aktifkan virtual environment
- Buka views.py yang terdapat pada subdirektori main, tambahkan import berikut: 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
- Tambahkan fungsi register (registrasi) pada views.py sebagai berikut:
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
- Buat berkas register.html pada direktori main/templates sebagai tampilan dari fungsi registrasi.
- Buka urls.py pada subdirektori main dan impor fungsi register
- Tambahkan path url ke dalam url patterns. Path url sebagai berikut"
path('register/', register, name='register'),
- Tambahkan fungsi login_user pada views.py sebagai berikut:
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
- Buat berkas login.html pada direktori main/templates sebagai tampilan dari fungsi login. 
- Buka urls.py pada subdirektori main dan impor fungsi login
- Tambahkan path url ke dalam url patterns. Path url sebagai berikut"
path('login/', login_user, name='login'),
- Tambahkan fungsi logout_user pada views.py sebagai berikut:
def logout_user(request):
    logout(request)
    return redirect('main:login')
- Buka berkas main.html dan tambahkan hyperlink tag untuk Add New Item Entry serta button logout.
- Buka urls.py pada subdirektori main dan impor fungsi logout_user
- Tambahkan path url ke dalam url patterns. Path url sebagai berikut"
path('logout/', logout_user, name='logout'),

b. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
step by step:
- Jalanlan proyek django pada local server.
- Buat dua akun User dengan registrasi terlebih dahulu.
- Login ke dalam kedua akun tersebut secara berurutan.
- Tambahkan tiga dummy data menggunakan model yang terlah dibuat pada setiap akun di lokal.

c. Menghubungkan model Product dengan User.
step by step: 
- Buka models.py pada subdirektori main dan lakukan impor model berikut:
from django.contrib.auth.models import User
- Pada class ItemEntry, tambahkan potongan kode berikut yang bertujuan agar satu Item Entry dapat diasosiasikan dengan satu user melalui sebuah relationship:
user = models.ForeignKey(User, on_delete=models.CASCADE)
- Buka views.py pada subdirektori main dan update dengan potongan kode berikut pada fungsi create_item_entry:
def create_mood_entry(request):
    form = MoodEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        mood_entry = form.save(commit=False)
        mood_entry.user = request.user
        mood_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_mood_entry.html", context)
- Ubah value pada item_entries dan context pada fungsi show_main dengan potongan kode berikut:
def show_main(request):
    mood_entries = MoodEntry.objects.filter(user=request.user)

    context = {
         'name': request.user.username,
         ...
    }
- Lakukan migrasi model untuk menyimpan semua perubahan dengan command berikut: python manage.py makemigrations
- Lakukan command berikut ini untuk mengaplikasikan migrasi yang dilakukan sebelumnya: python manage.py migrate
- Impor os dan ganti variabel DEBUG pada settings.py.

d. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
step by step:
- Buka views.py pada subdirektori main dan lakukan beberapa impor berikut:
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
- Pada fungsi login_user, tambahkan cookie bernama last_login untuk melihat kapan User terakhir kali login dengan mengganti kode pada blok conditional if form.is_valid dengan kode berikut:
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
- Pada fungsi show_main, tambahkan 'last_login' sebagai key dan request.COOKIES['last_login'] sebagai value pada context.
- Update fungsi logout_user sebagai berikut:
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
- Buka main.html dan tambahkan kode berikut setelah tombol logout untuk menampikan data last login dari User.
<h5>Sesi terakhir login: {{ last_login }}</h5>
- Buka views.py pada sub direktori main dan lakukan ubah value 'name' pada dictionary context menjadi request.user.username.
- Run proyek django untuk melihat tampilan informasi User yang sedang login seperti username dan cookies seperti last login.