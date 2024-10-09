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

Tugas 5
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Jawab:
Terdapat prioritas pengambilan CSS selector untuk suatu elemen HTML, yaitu:
a. Inline Style (Prioritas Tertinggi)
Gaya ini memiliki prioritas tertinggi karena secara langsung ditempatkan pada elemen dan override gaya lain dari sumber eksternal atau internal.
contoh: <p style="color: red;">This is a paragraph.</p>
Elemen <p> akan selalu berwarna merah, meskipun ada aturan color lain yang didefinisikan di stylesheet eksternal atau internal.

b. External dan Internal Style Sheets
Gaya ini didefinisikan di dalam <style> dalam internal atau dari eksternal. Gaya ini memiliki prioritas lebih rendah dari inline style, tetapi lebih tinggi dari default browser. Dalam hal ini, external dan internal style sheet memiliki urutan yang sama, tetapi gaya yang didefinisikan terakhir dalam cascading akan diterapkan jika ada konflik.

c. Browser Default (Prioritas Terendah)
Gaya default ini diterapkan jika tidak ada style lain yang diatur baik secara inline maupun dalam stylesheet.  

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Jawab: Desain yang respsonsif menjadi konsep penting dalam pengembangan aplikasi web karena beberapa alasan. Pertama, keragaman perangkat pengguna. Terdapat banyak pengguna yang mengakses suatu web dari berbagai perangkat, seperti hp, tablet, dekstop, dan lain-lain yang memiliki ukuran layar yang berbeda-beda sehingga diperlukan desain yang responsif. Kedua, efisiensi. Cukup dengan membuat satu desain yang responsif dan dapat memenuhi kebutuhan user dari berbagai perangkat dibandingkan dengan membuat berbagai desain yang mengakomodir masing-masing perangkat. Ketiga, web dapat menjangkau user yang lebih luas. Keempat, pemeliharaan dapat lebih mudah dikelola dengan satu situs web untuk seluruh perangkat. Contoh aplikasi dengan desain web yang responsif, seperti spotify, youtube, dan lain-lain. Contoh aplikasi dengan desain web yang belum responsif, seperti SIAK dan website yang saya buat saat ini.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Jawab: Ketiga komponen tersebut termasuk dalam box model CSS yang bertujuan untuk menentukan tata letak dan jarak antar elemen. Terdapat beberapa perbedaan dari ketiga komponen tersebut. 
a. Margin 
Margin merupakan ruang di luar batas elemen yang memisahkan elemen dari elemen-elemen di sekitarnya. Margin berada di luar border, transparan, dan dapat berupa bilangan negatif. Contoh implementasi:
margin: 10px;
margin-top: 10px;

b. Border
Border merupakan garis yang mengelilingi konten dan padding elemen. Border berada di antara margin dan padding yang dapat memiliki warna, gaya, dan ketebalan. Contoh implementasi:
border: 1px solid red; /
border-top: 1px solid red;

c. Padding
Padding merupakan ruang antara border dan konten elemen. Padding berada di dalam border yang dapat memiliki background yang sama dengan elemen serta hanya dapat bernilai positif. Contoh implementasi:
padding: 10px; //seluruh sisi akan berukuran 10px
padding-top: 10px; //sisi atas akan berukuran 10px

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Jawab: 
a. flex box 
flex box merupakan model tata letak satu dimensi yang memiliki fungsi utama untuk mengatur item dalam baris atau kolom. Flex box berguna untuk membuat desain yang responsif, mengatur alignment item secara vertikal atau horizontal, serta dapat mengubah urutan tampilan item tanpa mengubah HTML. Flex terdiri dari flex container dan flex items sebagai induk dan anak.

b. grid layout
Grid layout merupakan model tata letak dua dimensi yang memungkinkan pengembang untuk mengatur konten dalam baris dan kolom secara bersamaan. Grid layout berguna untuk menciptakan desain yang responsif, membuat layout yang kompleks secara mudah, serta mengatur konten dalam grid cells.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Jawab:
a. Implementasi fungsi untuk menghapus dan mengedit product
step-by-step:
- Buka views.py pada subdirektori main dan buat fungsi baru bernama edit_item dan delete_item yang menerima parameter request dan id. Berikut adalah kedua fungsi tersebut:

def edit_item(request, id):
    item = ItemEntry.objects.get(pk = id)

    form = ItemEntryForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

def delete_item(request, id):
    item = ItemEntry.objects.get(pk = id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

- Buat file html baru, yaitu edit_item.html sebagai template untuk edit item.
- Buka urls.py yang ada pada subdirektori main dan import fungsi edit_item dan delete_item.
- Tambahkan path url ke dalam url patterns untuk mengakses fungsi edit_item dan delete_item.

b. Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
step-by-step:
- Menambahkan global.css pada direktori static/css.
- Hubungkan global.css dan script Tailwind ke base.html
- Isi file global.css dengan berikut:
.form-style form input, form textarea, form select {
    width: 100%;
    padding: 0.5rem;
    border: 2px solid #bcbcbc;
    border-radius: 0.375rem;
}
.form-style form input:focus, form textarea:focus, form select:focus {
    outline: none;
    border-color: #674ea7;
    box-shadow: 0 0 0 3px #674ea7;
}
@keyframes shine {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}
.animate-shine {
    background: linear-gradient(120deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.3));
    background-size: 200% 100%;
    animation: shine 3s infinite;
}

- Melakukan styling pada halaman login dengan mengubah file login.html menjadi seperti berikut:
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center w-screen bg-red-200 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8">
    <div>
      <h2 class="mt-6 text-center text-black text-3xl font-extrabold text-gray-900">
        Login to your account
      </h2>
    </div>
    <form class="mt-8 space-y-6" method="POST" action="">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
        <div>
          <label for="username" class="sr-only">Username</label>
          <input id="username" name="username" type="text" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Username">
        </div>
        <div>
          <label for="password" class="sr-only">Password</label>
          <input id="password" name="password" type="password" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Password">
        </div>
      </div>

      <div>
        <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-orange-600 hover:bg-orange-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500">
          Sign in
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      {% if message.tags == "success" %}
            <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% elif message.tags == "error" %}
            <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% else %}
            <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% endif %}
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-black">
        Don't have an account yet?
        <a href="{% url 'main:register' %}" class="font-medium text-black-200 hover:text-orange-300">
          Register Now
        </a>
      </p>
    </div>
  </div>
</div>
{% endblock content %}

- Styling halaman register dengan mengubah file register.html dengan sebagai berikut:
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center bg-red-200 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8 form-style">
    <div>
      <h2 class="mt-6 text-center text-3xl font-extrabold text-black">
        Create your account
      </h2>
    </div>
    <form class="mt-8 space-y-6" method="POST">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
        {% for field in form %}
          <div class="{% if not forloop.first %}mt-4{% endif %}">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
              {{ field.label }}
            </label>
            <div class="relative">
              {{ field }}
              <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                {% if field.errors %}
                  <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                  </svg>
                {% endif %}
              </div>
            </div>
            {% if field.errors %}
              {% for error in field.errors %}
                <p class="mt-1 text-sm text-red-600">{{ error }}</p>
              {% endfor %}
            {% endif %}
          </div>
        {% endfor %}
      </div>

      <div>
        <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-orange-600 hover:bg-orange-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
          Register
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
        <span class="block sm:inline">{{ message }}</span>
      </div>
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-black">
        Already have an account?
        <a href="{% url 'main:login' %}" class="font-medium text-black-200 hover:text-indigo-300">
          Login here
        </a>
      </p>
    </div>
  </div>
</div>
{% endblock content %}

- Styling halaman tambah product dengan membuat file baru, yaitu card_item.html pada main/templates. Lalu, isi file tersebut dengan kode berikut:
<div class="max-w-sm w-full min-h-[200px] mx-auto bg-red-400 rounded-xl shadow-lg overflow-hidden transition-all duration-300 hover:shadow-xl border-4 border-black">  <div class="p-6">
    <div class="bg-red text-white font-bold text-2xl mb-4 p-3 rounded-md text-center shadow-md border-4 border-black">
      {{item_entry.name}}
    </div>
    <p class="font-bold text-white">PRICE</p>
    <p class="text-black-600 mb-4">{{item_entry.price}}</p>
    <p class="font-bold text-white">DESCRIPTION</p>
    <p class="text-black-700 mb-4">{{item_entry.description}}</p>
    <div class="flex justify-end space-x-2">
      <a href="{% url 'main:edit_item' item_entry.pk %}" class="bg-yellow-500 hover:bg-blue-600 text-white font-medium py-2 px-4 rounded border-2 border-black hover:border-blue-400 transition duration-300">
        Edit
      </a>
      <a href="{% url 'main:delete_item' item_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white font-medium py-2 px-4 rounded border-2 border-black hover:border-red-700 transition duration-300">
        Delete
      </a>
    </div>
  </div>
</div>

c. Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
step-by-step(masih berhubungan dengan step sebelumnya):
- Untuk menampilkan gambar apabila item entry masih kosong, maka tambahkan foto dengan nama sedih-banget.png pada direktori static/image.
- Modifikasi main.html agar main.html dapat menggunakan sedih-banget.png.

d. Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).
step-by-step(masih berhubungan dengan step sebelumnya):
- Modifikasi main.html agar main.html dapat menggunakan card_item.html.
- Item berhasil ditampilkan dalam bentuk card.

e. Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
step-by-step: 
- Buat file edit_item.html yang berfungsi untuk menampilkan halaman ketika button edit ditekan. Berikut adalah kode pada file tersebut.
{% extends 'base.html' %}
{% load static %}
{% block meta %}
<title>Edit Item</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}
<div class="flex flex-col min-h-screen bg-gray-100">
  <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
    <h1 class="text-3xl font-bold text-center mb-8 text-black">Edit Item Entry</h1>
  
    <div class="bg-white rounded-lg p-6 form-style">
      <form method="POST" class="space-y-6">
          {% csrf_token %}
          {% for field in form %}
              <div class="flex flex-col">
                  <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                      {{ field.label }}
                  </label>
                  <div class="w-full">
                      {{ field }}
                  </div>
                  {% if field.help_text %}
                      <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                  {% endif %}
                  {% for error in field.errors %}
                      <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                  {% endfor %}
              </div>
          {% endfor %}
          <div class="flex justify-center mt-6">
              <button type="submit" class="bg-indigo-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-indigo-700 transition duration-300 ease-in-out w-full">
                  Edit Item Entry
              </button>
          </div>
      </form>
  </div>
  </div>
</div>
{% endblock %}

- Tambahkan button edit yang akan mengarahkan ke url edit_item. Berikut kodenya:
<div class="flex justify-end space-x-2">
      <a href="{% url 'main:edit_item' item_entry.pk %}" class="bg-yellow-500 hover:bg-blue-600 text-white font-medium py-2 px-4 rounded border-2 border-black hover:border-blue-400 transition duration-300">
        Edit
      </a>
      ...
    </div>

- Tambahkan button delete yang akan mengarahkan ke url delete_item. Berikut kodenya:
<div class="flex justify-end space-x-2">
    ....
    <a href="{% url 'main:delete_item' item_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white font-medium py-2 px-4 rounded border-2 border-black hover:border-red-700 transition duration-300">
        Delete
      </a>
</div>

f. Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
step-by-step:
- Buat file baru dengan nama navbar.html pada direktori templates di root. Isi dengan kode berikut:

<nav class="bg-black shadow-lg fixed top-0 left-0 z-40 w-screen">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      <div class="flex items-center">
        <h1 class="text-2xl font-bold text-center text-white">Arlic Good Shop</h1>
      </div>
      <div class="hidden md:flex items-center">
        {% if user.is_authenticated %}
          <span class="text-white mr-4">Welcome, {{ user.username }} !</span>
          <a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Logout
          </a>
        {% else %}
          <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">
            Login
          </a>
          <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Register
          </a>
        {% endif %}
      </div>
      <div class="md:hidden flex items-center">
        <button class="mobile-menu-button">
          <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
            <path d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
        </button>
      </div>
    </div>
  </div>
  <!-- Mobile menu -->
  <div class="mobile-menu hidden md:hidden  px-4 w-full md:max-w-full">
    <div class="pt-2 pb-3 space-y-1 mx-auto">
      {% if user.is_authenticated %}
        <span class="block text-gray-300 px-3 py-2">Welcome, {{ user.username }}</span>
        <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
          Logout
        </a>
      {% else %}
        <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
          Login
        </a>
        <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
          Register
        </a>
      {% endif %}
    </div>
  </div>
  <script>
    const btn = document.querySelector("button.mobile-menu-button");
    const menu = document.querySelector(".mobile-menu");
  
    btn.addEventListener("click", () => {
      menu.classList.toggle("hidden");
    });
  </script>
</nav>

- Hubungkan navbar tersebut ke dalam main.html, create_item_entry.html, dan edit_item.html yang ada pada subdirektori main/templates dengan kode berikut:
{% extends 'base.html' %}
{% block content %}
{% include 'navbar.html' %}
...
{% endblock content%}

Tugas 6
 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
 Jawab: JavaScript merupakan bahasa pemrograman multi-paradigma tingkat tinggi lintas platform yang membuat JavaScript mendukung konsep pemrograman berbasis objek, pemrograman imperatif, dan pemrograman fungsional. Dalam pengembangan aplikasi web, JavaScript memiliki beberapa manfaat, yaitu manipulasi halaman web dapat dilakukan secara dinamis serta memungkinkan halaman web untuk berinteraksi secara dinamis dengan pengguna, digunakan untuk styling css dan html secara dinamis tanpa perlu memuat ulang halaman, digunakan untuk pengolahan Client-Side, digunakan di berbagai perangkat & peramban, dan lain sebagainya.


 2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Jawab: Fungsi penggunaan await ketika menggunakan fetch() adalah untuk menunggu hasil dari operasi asinkronus yang dijalankan oleh fetch(). Fetch API mengembalikan sebuah Promise, yang berarti proses pengambilan data dari server dilakukan secara asinkron, dan hasilnya mungkin tidak langsung tersedia. Dengan menggunakan await, kita dapat menunggu hasil dari fetch() hingga selesai sebelum melanjutkan eksekusi kode, sehingga kita bisa mendapatkan respons yang diinginkan secara sinkron dalam bentuk objek Response.

Jika kita tidak menggunakan await pada pemanggilan fetch(), kode akan terus dieksekusi sebelum hasil dari fetch() tersedia. Ini berarti kita akan mendapatkan Promise sebagai hasil dari fetch(), bukan data yang sudah diproses. Sebagai contoh, jika kita mencoba untuk langsung menggunakan hasil fetch() tanpa await, kita tidak akan bisa mengakses respons atau data yang diambil, karena permintaan HTTP belum selesai.

 3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Jawab: Kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST karena decorator ini mencegah Django dari melakukan pengecekan keberadaan CSRF token pada permintaan POST yang dikirimkan ke fungsi tersebut. Dalam kondisi normal, Django secara default memeriksa CSRF token pada setiap permintaan POST untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF).

Namun, dalam konteks AJAX POST, terutama jika tidak menggunakan CSRF token dalam permintaan, Django akan menolak permintaan tersebut karena tidak ada token yang valid. Oleh karena itu, dengan menambahkan @csrf_exempt pada view, kita dapat menghindari pengecekan ini sehingga request AJAX dapat diproses meskipun tidak ada CSRF token.


 4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Jawab: Dengan melakukan pembersihan data di backend (misalnya, menggunakan strip_tags dan DOMPurify seperti yang diterapkan pada tutorial PBP), kita memastikan bahwa data yang masuk ke server sudah aman dan bebas dari potensi serangan seperti Cross-Site Scripting (XSS) atau injeksi lainnya. Backend merupakan tempat yang lebih dapat dipercaya, karena kontrol penuh ada pada pengembang, berbeda dengan frontend yang rentan dimanipulasi oleh pengguna.

 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Jawab:
a. Mengimplementasikan AJAX GET.
Step-by-step: 
- Buka berkas views.py dan hapus dua baris berikut: 
item_entries = ItemEntry.objects.filter(user=request.user)
'item_entries': item_entries,
- Buka berkas views.py dan ubah baris pertama pada fungsi show_json dan show_xml dengan kode berikut
data = ItemEntry.objects.filter(user=request.user)
- Buka berkas main.html dan hapus bagian conditional item_entries yang menampilkan card_item ketika kosong atau tidak.
- Di bagian conditional yang telah dihapus tadi, tambahkan kode berikut:
<div id="item_entry_cards"></div>
- Buat block script sebelum {% endblock content %} dan buat fungsi baru dengan nama getItemEntries seperti berikut:
<script>
  async function getItemEntries(){
      return fetch("{% url 'main:show_json' %}").then((res) => res.json())
  }
</script>
- Buat fungsi baru pada block script dengan nama refreshItemEntries untuk me-refresh data item secara asinkronus seperti berikut:
async function refreshItemEntries() {
    document.getElementById("item_entry_cards").innerHTML = "";
    document.getElementById("item_entry_cards").className = "";
    const itemEntries = await getItemEntries();
    let htmlString = "";
    let classNameString = "";

    if (itemEntries.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'image/sedih-banget.jpg' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">Belum ada data item pada Arlic Good Shop.</p>
            </div>
        `;
    }
    else {
        classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full"
        itemEntries.forEach((item) => {
            const name = DOMPurify.sanitize(item.fields.name);
            const price = DOMPurify.sanitize(item.fields.price);
            const description = DOMPurify.sanitize(item.fields.description);
            htmlString += `
            <div class="max-w-sm w-full min-h-[200px] mx-auto bg-red-400 rounded-xl shadow-lg overflow-hidden transition-all duration-300 hover:shadow-xl border-4 border-black">  <div class="p-6">
    <div class="bg-red text-white font-bold text-2xl mb-4 p-3 rounded-md text-center shadow-md border-4 border-black">
      ${item.fields.name}
    </div>
    <p class="font-bold text-white">PRICE</p>
    <p class="text-black-600 mb-4">${item.fields.price}</p>
    <p class="font-bold text-white">DESCRIPTION</p>
    <p class="text-black-700 mb-4">${item.fields.description}</p>
    <div class="flex justify-end space-x-2">
      <a href="/edit-item/${item.pk}"class="bg-yellow-500 hover:bg-blue-600 text-white font-medium py-2 px-4 rounded border-2 border-black hover:border-blue-400 transition duration-300">
        Edit
      </a>
      <a href="/delete/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white font-medium py-2 px-4 rounded border-2 border-black hover:border-red-700 transition duration-300">
        Delete
      </a>
    </div>
  </div>
</div>
            `;
        });
    }
b. Mengimplementasikan AJAX POST
step-by-step:
- Impor dua hal berikut di views.py:
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
- Buat fungsi baru dengan nama add_item_entry_ajax yang menerima parameter request dengan kode berikut:
...
@csrf_exempt
@require_POST
def add_item_entry_ajax(request):
    name = strip_tags(request.POST.get("name")) # strip HTML tags!
    price = strip_tags(request.POST.get("price")) # strip HTML tags!
    description = strip_tags(request.POST.get("description")) # strip HTML tags!
    user = request.user
    new_item = ItemEntry(
        name=name, price=price,
        description=description,
        user=user
    )
    new_item.save()
    return HttpResponse(b"CREATED", status=201)
    ...
CATATAN: menambahkan strip_tags agar aplikasi terlindungi dari cross site scripting dengan membersihkan data baru. Hal tersebut juga diimplementasikan di forms.py untuk masing-masing model.

- Buka urls.py dan impor fungsi add_item_entry_ajax.
- Tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor.
- Tambahkan kode berikut untuk mengimplementasikan modal (Tailwind) dibawah div dengan id item_entry_cards:
</div>
    <div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
      <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
        <!-- Modal header -->
        <div class="flex items-center justify-between p-4 border-b rounded-t">
          <h3 class="text-xl font-semibold text-gray-900">
            Add New Item Entry
          </h3>
          <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
            <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
            </svg>
            <span class="sr-only">Close modal</span>
          </button>
        </div>
        <!-- Modal body -->
        <div class="px-6 py-4 space-y-6 form-style">
          <form id="itemEntryForm">
            <div class="mb-4">
              <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
              <input type="text" id="name" name="name" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter your item name" required>
            </div>
            <div class="mb-4">
              <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
              <input type="number" id="price" name="price" min="0" rows="3" class="mt-1 block w-full resize-none border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter the price" required>
            </div>
            <div class="mb-4">
              <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
              <textarea id="description" name="description" min="1" max="10" class="mt-1 h-32 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" required></textarea>
            </div>
          </form>
        </div>
        <!-- Modal footer -->
        <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
          <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
          <button type="submit" id="submitItemEntry" form="itemEntryForm" class="bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
        </div>
      </div>
    </div>
</div>

- Agar modal dapat berfungsi, tambahkan fungsi-fungsi javascript berikut:
<script>
...
  const modal = document.getElementById('crudModal');
  const modalContent = document.getElementById('crudModalContent');

  function showModal() {
      const modal = document.getElementById('crudModal');
      const modalContent = document.getElementById('crudModalContent');

      modal.classList.remove('hidden'); 
      setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
      }, 50); 
  }

  function hideModal() {
      const modal = document.getElementById('crudModal');
      const modalContent = document.getElementById('crudModalContent');

      modalContent.classList.remove('opacity-100', 'scale-100');
      modalContent.classList.add('opacity-0', 'scale-95');

      setTimeout(() => {
        modal.classList.add('hidden');
      }, 150); 
  }

  document.getElementById("cancelButton").addEventListener("click", hideModal);
  document.getElementById("closeModalBtn").addEventListener("click", hideModal);
...
</script>

- Tambahkan tombol baru untuk melakukan penambahan data dengan AJAX di bawah tombol Add New Item Entry seperti berikut:
<a href="{% url 'main:create_item_entry' %}" class="bg-orange-600 hover:bg-orange-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
            Add New Item Entry
        </a>
        <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">
          Add New Item Entry by AJAX
        </button>

- Tambahkan fungsi baru pada block script dengan nama addItemEntry seperti berikut:
function addItemEntry() {
    fetch("{% url 'main:add_item_entry_ajax' %}", {
      method: "POST",
      body: new FormData(document.querySelector('#itemEntryForm')),
    })
    .then(response => refreshItemEntries())

    document.getElementById("itemEntryForm").reset(); 
    document.querySelector("[data-modal-toggle='crudModal']").click();

    return false;
  }

- Tambahkan sebuah event listener pada form yang ada di modal untuk menjalankan fungsi addItemEntry() sebagai berikut:
document.getElementById("itemEntryForm").addEventListener("submit", (e) => {
    e.preventDefault();
    addItemEntry();