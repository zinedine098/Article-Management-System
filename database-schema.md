Siap. Ini aku susun **struktur database LENGKAP, rapi, dan siap kamu taruh di README / dokumentasi**.
Aku sertakan **kolom, tipe data, status/constraint, dan keterangan** biar kelihatan profesional.

---

# 🗄️ STRUKTUR DATABASE

**Blog / Article Management System (Django)**

---

## 1️⃣ `accounts_user`

(**Custom User – pusat auth & role**)

| Kolom        | Tipe Data    | Status           | Keterangan                |
| ------------ | ------------ | ---------------- | ------------------------- |
| id           | BIGINT       | PK, Auto         | Primary key               |
| username     | VARCHAR(150) | UNIQUE, NOT NULL | Username                  |
| email        | VARCHAR(255) | UNIQUE, NOT NULL | Email                     |
| password     | VARCHAR      | NOT NULL         | Hashed password           |
| role         | ENUM         | DEFAULT `user`   | `admin`, `author`, `user` |
| is_active    | BOOLEAN      | DEFAULT TRUE     | User aktif / tidak        |
| is_staff     | BOOLEAN      | DEFAULT FALSE    | Akses admin               |
| is_superuser | BOOLEAN      | DEFAULT FALSE    | Super admin               |
| last_login   | DATETIME     | NULLABLE         | Login terakhir            |
| date_joined  | DATETIME     | AUTO             | Tanggal daftar            |

---

## 2️⃣ `articles_category`

| Kolom      | Tipe Data    | Status           | Keterangan    |
| ---------- | ------------ | ---------------- | ------------- |
| id         | BIGINT       | PK, Auto         | Primary key   |
| name       | VARCHAR(100) | NOT NULL         | Nama kategori |
| slug       | VARCHAR(120) | UNIQUE, NOT NULL | SEO URL       |
| created_at | DATETIME     | AUTO             | Dibuat        |

---

## 3️⃣ `articles_tag`

| Kolom | Tipe Data   | Status   | Keterangan  |
| ----- | ----------- | -------- | ----------- |
| id    | BIGINT      | PK, Auto | Primary key |
| name  | VARCHAR(50) | NOT NULL | Nama tag    |
| slug  | VARCHAR(60) | UNIQUE   | SEO         |

---

## 4️⃣ `articles_article`

(**Core table – paling penting**)

| Kolom       | Tipe Data    | Status           | Keterangan                       |
| ----------- | ------------ | ---------------- | -------------------------------- |
| id          | BIGINT       | PK, Auto         | Primary key                      |
| title       | VARCHAR(255) | NOT NULL         | Judul                            |
| slug        | VARCHAR(255) | UNIQUE, NOT NULL | URL artikel                      |
| content     | TEXT         | NOT NULL         | Isi artikel                      |
| thumbnail   | VARCHAR      | NULLABLE         | Path gambar                      |
| status      | ENUM         | DEFAULT `draft`  | `draft`, `published`, `archived` |
| author_id   | BIGINT       | FK → user.id     | Penulis                          |
| category_id | BIGINT       | FK, NULLABLE     | Kategori                         |
| view_count  | INT          | DEFAULT 0        | Hit artikel                      |
| created_at  | DATETIME     | AUTO             | Dibuat                           |
| updated_at  | DATETIME     | AUTO             | Diupdate                         |
| deleted_at  | DATETIME     | NULLABLE         | Soft delete                      |

---

## 5️⃣ `articles_article_tags`

(**Pivot table – Many to Many**)

| Kolom      | Tipe Data | Status          | Keterangan  |
| ---------- | --------- | --------------- | ----------- |
| id         | BIGINT    | PK, Auto        | Primary key |
| article_id | BIGINT    | FK → article.id | Artikel     |
| tag_id     | BIGINT    | FK → tag.id     | Tag         |

📌 *Biasanya dibuat otomatis oleh Django*

---

## 6️⃣ `comments_comment`

| Kolom       | Tipe Data | Status          | Keterangan        |
| ----------- | --------- | --------------- | ----------------- |
| id          | BIGINT    | PK, Auto        | Primary key       |
| article_id  | BIGINT    | FK → article.id | Artikel           |
| user_id     | BIGINT    | FK → user.id    | User              |
| parent_id   | BIGINT    | FK, NULLABLE    | Reply ke komentar |
| content     | TEXT      | NOT NULL        | Isi komentar      |
| is_approved | BOOLEAN   | DEFAULT FALSE   | Moderasi          |
| created_at  | DATETIME  | AUTO            | Dibuat            |

---

## 7️⃣ `pages_page` (OPSIONAL – kalau mau CMS Page)

| Kolom        | Tipe Data    | Status       | Keterangan     |
| ------------ | ------------ | ------------ | -------------- |
| id           | BIGINT       | PK, Auto     | Primary key    |
| title        | VARCHAR(150) | NOT NULL     | Judul          |
| slug         | VARCHAR(150) | UNIQUE       | URL            |
| content      | TEXT         | NOT NULL     | Isi            |
| is_published | BOOLEAN      | DEFAULT TRUE | Tampil / tidak |
| created_at   | DATETIME     | AUTO         | Dibuat         |

---

# 🔗 RELASI DATABASE (SUMMARY)

| Relasi             | Tipe          |
| ------------------ | ------------- |
| User → Article     | One to Many   |
| Category → Article | One to Many   |
| Article → Tag      | Many to Many  |
| Article → Comment  | One to Many   |
| Comment → Comment  | Self Relation |

---

# 📌 STATUS ENUM YANG DIGUNAKAN

### 🔹 User Role

```
admin
author
user
```

### 🔹 Article Status

```
draft        → hanya author & admin
published    → publik
archived     → disembunyikan
```

### 🔹 Comment Status

```
is_approved = false → pending
is_approved = true  → tampil
```

---

# 💎 KENAPA STRUKTUR INI KUAT?

✔ Real-world CMS
✔ Siap scaling
✔ Aman (soft delete, moderation)
✔ Mudah jadi REST API
✔ Mudah dijelaskan saat interview

---

## 🚀 NEXT STEP PALING LOGIS

Setelah database **fixed**, langkah berikutnya:

1️⃣ Mapping ke **Django Models** (final version)
2️⃣ Buat **migration & superuser**
3️⃣ Register ke **Django Admin**

Kalau kamu mau, aku bisa:

* Turunkan ini ke **models.py final**
* Buatin **ERD diagram visual**
* Atau **cek ulang apakah terlalu kompleks / terlalu simpel**

Tinggal bilang mau lanjut ke mana 👌
