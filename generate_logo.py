from pathlib import Path

svg = '''
<svg width="1200" height="260" viewBox="0 0 1200 260" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="g1" x1="0" y1="0" x2="170" y2="170" gradientUnits="userSpaceOnUse">
      <stop stop-color="#0F172A"/>
      <stop offset="0.5" stop-color="#2563EB"/>
      <stop offset="1" stop-color="#14B8A6"/>
    </linearGradient>
  </defs>

  <rect width="1200" height="260" fill="#F8FAFC"/>

  <g transform="translate(20,20)">
    <rect x="0" y="0" width="170" height="170" rx="38" fill="url(#g1)"/>
    <path d="M118 39C95 22 63 23 40 43C18 62 18 93 39 108L77 135C90 144 97 154 97 166C97 180 87 191 70 191H52C45 191 40 186 40 179V156C40 149 45 144 52 144H70C82 144 90 137 90 127C90 118 83 111 70 104L42 88C24 80 12 67 12 50C12 31 28 18 52 18H110C121 18 129 25 129 36V60C129 71 121 78 110 78H82C70 78 63 84 63 92C63 100 70 106 82 106H109C129 106 145 119 145 137C145 155 131 168 110 168H78C70 168 64 162 64 154V140C64 133 70 127 78 127H91C101 127 108 121 108 111C108 102 101 96 91 96H50C38 96 29 90 29 79V38C29 30 36 24 44 24H110C119 24 126 30 126 38V39H118Z" fill="white"/>
    <path d="M35 114L71 81L100 100L141 62" stroke="#E0ECFF" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="35" cy="114" r="6" fill="#E0ECFF"/>
    <circle cx="141" cy="62" r="6" fill="#E0ECFF"/>
  </g>

  <g transform="translate(230,58)">
    <text x="0" y="56" font-size="62" font-family="Segoe UI, Arial, sans-serif" font-weight="800" fill="#0F172A" letter-spacing="1.5">SILIXUS</text>
    <text x="2" y="96" font-size="18" font-family="Segoe UI, Arial, sans-serif" font-weight="700" fill="#475569" letter-spacing="5">SOFTWARE • AI • DEVOPS</text>
    <rect x="0" y="122" width="350" height="5" rx="2.5" fill="url(#g1)"/>
  </g>
</svg>
'''

output_path = Path(__file__).resolve().parent / 'silixus_logo.svg'
output_path.write_text(svg, encoding='utf-8')
print(f'Logo generated: {output_path}')
