#!/usr/bin/env python3

# Script to generate individual slide HTML files in FINAL SLIDES folder

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bubl - Slide {slide_num}</title>
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Stylesheets -->
    <link rel="stylesheet" href="../css/styles.css">
    
    <!-- Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
    
    <!-- Box Icons for modern iconography -->
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
</head>
<body>
    <!-- Progress Bar -->
    <div class="progress-container">
        <div id="progressBar" class="progress-bar" style="width: {progress_percent}%;"></div>
    </div>
    
    <!-- Slides Container -->
    <div class="slides-container">
        <!-- Slide {slide_num}: Empty Template -->
        <section id="slide-{slide_num}" class="slide active">
            <div class="slide-content {bg_class}">
                <!-- Empty content area to be populated -->
            </div>
        </section>
    </div>
    
    <!-- Navigation Controls -->
    <div class="navigation-controls">
        <button id="prevBtn" class="nav-button"><i class='bx bx-chevron-left'></i> Previous</button>
        <button id="nextBtn" class="nav-button primary">Next <i class='bx bx-chevron-right'></i></button>
    </div>
    
    <!-- Navigation Dots -->
    <div id="navDots" class="nav-dots"></div>
    
    <!-- Slide Counter -->
    <div class="slide-counter">
        <div class="indicator"></div>
        <span id="slideCounter">{slide_num_padded}</span>
        <span>/</span>
        <span id="slideCounterTotal">12</span>
    </div>
    
    <!-- Scripts -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            // Set up navigation between files
            const prevBtn = document.getElementById('prevBtn');
            const nextBtn = document.getElementById('nextBtn');
            const navDots = document.getElementById('navDots');
            const currentSlideNumber = {slide_num};
            const totalSlides = 12;
            
            // Create navigation dots
            for (let i = 0; i < totalSlides; i++) {{
                const dot = document.createElement('div');
                dot.classList.add('nav-dot');
                if (i === currentSlideNumber - 1) dot.classList.add('active');
                dot.addEventListener('click', () => goToSlide(i + 1));
                navDots.appendChild(dot);
            }}
            
            // Navigation functions
            function goToSlide(slideNumber) {{
                window.location.href = `slide${{slideNumber}}.html`;
            }}
            
            // Event listeners
            prevBtn.addEventListener('click', () => {{
                if (currentSlideNumber > 1) {{
                    goToSlide(currentSlideNumber - 1);
                }}
            }});
            
            nextBtn.addEventListener('click', () => {{
                if (currentSlideNumber < totalSlides) {{
                    goToSlide(currentSlideNumber + 1);
                }}
            }});
            
            // Keyboard navigation
            document.addEventListener('keydown', (e) => {{
                if (e.key === 'ArrowRight' || e.key === 'PageDown') {{
                    if (currentSlideNumber < totalSlides) {{
                        goToSlide(currentSlideNumber + 1);
                    }}
                }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
                    if (currentSlideNumber > 1) {{
                        goToSlide(currentSlideNumber - 1);
                    }}
                }}
            }});
        }});
    </script>
</body>
</html>"""

backgrounds = {
    3: "gradient-subtle",
    4: "gradient-subtle",
    5: "gradient-subtle",
    6: "style=\"background: linear-gradient(135deg, #F2FFFD 0%, #E9F9FF 100%);\"",
    7: "style=\"background: linear-gradient(135deg, #FFF6F9 0%, #FFF0F7 100%);\"",
    8: "gradient-subtle",
    9: "gradient-subtle",
    10: "gradient-subtle",
    11: "gradient-subtle",
    12: "gradient-subtle"
}

# Generate slides 3-12
for i in range(3, 13):
    slide_num = i
    progress_percent = (i / 12) * 100
    bg_class = backgrounds[i]
    slide_num_padded = str(i).zfill(2)
    
    content = template.format(
        slide_num=slide_num,
        progress_percent=progress_percent,
        bg_class=bg_class,
        slide_num_padded=slide_num_padded
    )
    
    with open(f"slide{i}.html", "w") as f:
        f.write(content)
    
    print(f"Created slide{i}.html")

# Create index.html to redirect to slide1
index_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bubl - Presentation</title>
    <meta http-equiv="refresh" content="0;url=slide1.html">
</head>
<body>
    <p>Redirecting to <a href="slide1.html">first slide</a>...</p>
</body>
</html>"""

with open("index.html", "w") as f:
    f.write(index_content)

print("Created index.html")
print("All slide files created successfully!") 