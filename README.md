<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kelas TI 1D - Linktree</title>
    <style>
        /* Reset dan Base Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #1a2a6c, #b21f1f, #fdbb2d);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            color: #fff;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
        }
        
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .container {
            width: 100%;
            max-width: 500px;
            margin: 0 auto;
            text-align: center;
        }
        
        /* Header Styles */
        .profile {
            margin-bottom: 30px;
        }
        
        .profile-img {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            border: 5px solid rgba(255, 255, 255, 0.3);
            margin-bottom: 15px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }
        
        .profile h1 {
            font-size: 28px;
            margin-bottom: 5px;
            text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
        }
        
        .profile p {
            font-size: 16px;
            opacity: 0.9;
            margin-bottom: 20px;
        }
        
        /* Link Styles */
        .links {
            width: 100%;
            margin-bottom: 30px;
        }
        
        .link-item {
            background-color: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 12px;
            margin-bottom: 15px;
            padding: 15px;
            transition: all 0.3s ease;
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .link-item:hover {
            transform: translateY(-5px);
            background-color: rgba(255, 255, 255, 0.2);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
        }
        
        .link-item a {
            text-decoration: none;
            color: white;
            font-weight: 500;
            font-size: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }
        
        .link-icon {
            width: 24px;
            height: 24px;
        }
        
        /* Footer Styles */
        .footer {
            margin-top: auto;
            padding: 20px 0;
            font-size: 14px;
            opacity: 0.7;
        }
        
        /* Responsive */
        @media (max-width: 600px) {
            .container {
                padding: 0 15px;
            }
            
            .profile-img {
                width: 120px;
                height: 120px;
            }
            
            .profile h1 {
                font-size: 24px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Profile Section -->
        <div class="profile">
            <img src="https://via.placeholder.com/150" alt="Foto Kelas TI 1D" class="profile-img">
            <h1>Kelas TI 1D</h1>
            <p>Teknik Informatika - Angkatan 2023/2024</p>
        </div>
        
        <!-- Links Section -->
        <div class="links">
            <div class="link-item">
                <a href="#">
                    <svg class="link-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/>
                    </svg>
                    Grup WhatsApp Kelas
                </a>
            </div>
            
            <div class="link-item">
                <a href="#">
                    <svg class="link-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
                    </svg>
                    Email Kelas
                </a>
            </div>
            
            <div class="link-item">
                <a href="#">
                    <svg class="link-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
                    </svg>
                    Jadwal Kuliah
                </a>
            </div>
            
            <div class="link-item">
                <a href="#">
                    <svg class="link-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/>
                    </svg>
                    Materi Perkuliahan
                </a>
            </div>
            
            <div class="link-item">
                <a href="#">
                    <svg class="link-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
                    </svg>
                    Daftar Mahasiswa
                </a>
            </div>
            
            <div class="link-item">
                <a href="#">
                    <svg class="link-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
                    </svg>
                    Galeri Foto Kelas
                </a>
            </div>
        </div>
        
        <!-- Footer -->
        <div class="footer">
            <p>&copy; 2023 Kelas TI 1D - Teknik Informatika</p>
        </div>
    </div>

    <script>
        // Animasi untuk link saat dihover
        document.querySelectorAll('.link-item').forEach(item => {
            item.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-5px)';
            });
            
            item.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0)';
            });
        });
        
        // Tambahkan efek klik pada link
        document.querySelectorAll('.link-item a').forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                
                // Animasi klik
                this.parentElement.style.transform = 'scale(0.95)';
                setTimeout(() => {
                    this.parentElement.style.transform = 'scale(1)';
                }, 150);
                
                // Di sini Anda bisa menambahkan logika untuk membuka link yang sesuai
                alert('Link: ' + this.textContent.trim());
            });
        });
    </script>
</body>
</html>
