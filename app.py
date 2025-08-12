import streamlit as st

html_code = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Infotech Soluções</title>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;500;700&display=swap" rel="stylesheet">
  <style>
    body {
      margin: 0;
      font-family: 'Roboto', sans-serif;
      background-color: #f4f4f4;
      color: #333;
    }
    header {
      background-color: #2c3e50;
      color: white;
      padding: 1.5rem;
      text-align: center;
    }
    nav a {
      color: white;
      margin: 0 1rem;
      text-decoration: none;
      font-weight: bold;
    }
    .hero {
      padding: 2rem;
      text-align: center;
      background: #ecf0f1;
    }
    .hero h1, .hero h2 {
      margin-bottom: 1rem;
    }
    .services {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 2rem;
      padding: 2rem;
    }
    .card {
      background: white;
      padding: 1.5rem;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    .card h3 {
      color: #2c3e50;
    }
    .card a {
      display: inline-block;
      margin-top: 1rem;
      color: #2980b9;
      text-decoration: none;
      font-weight: bold;
    }
    .card a:hover {
      text-decoration: underline;
    }
    footer {
      text-align: center;
      padding: 1rem;
      background-color: #2c3e50;
      color: white;
      margin-top: 2rem;
    }
    form {
      max-width: 400px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
    input, textarea, button {
      padding: 0.75rem;
      border: 1px solid #ccc;
      border-radius: 5px;
      font-family: 'Roboto', sans-serif;
    }
    button {
      background-color: #2c3e50;
      color: white;
      border: none;
      cursor: pointer;
    }
    button:hover {
      background-color: #1a242f;
    }
    .whatsapp-float {
      position: fixed;
      bottom: 20px;
      right: 20px;
      z-index: 100;
    }
    .whatsapp-float img {
      width: 60px;
      height: 60px;
      transition: transform 0.3s ease;
    }
    .whatsapp-float img:hover {
      transform: scale(1.1);
    }
  </style>
</head>
<body>
  <header>
    <h1>Infotech Soluções</h1>
    <nav>
      <a href="#servicos">Serviços</a>
      <a href="#sobre">Sobre</a>
      <a href="#contato">Contato</a>
    </nav>
  </header>

  <section class="hero">
    <h1>Aprendizado digital sem complicação</h1>
    <p>Cursos e suporte acessível em informática e tecnologia</p>
  </section>

  <section class="services" id="servicos">
    <div class="card">
      <h3>Aulas Particulares</h3>
      <p>Aprenda no seu ritmo: Windows, Word, Excel, navegação segura e muito mais.</p>
      <a href="agendamento.html">Agende uma aula</a>
    </div>
    <div class="card">
      <h3>Infotech Aprenda</h3>
      <p>Acesso a recursos educacionais exclusivos, com <strong>dicas de informática</strong>, vídeos tutoriais e materiais de apoio.</p>
      <a href="#">Acessar recursos</a>
    </div>
    <div class="card">
      <h3>Atendimento a Domicílio</h3>
      <p>Levamos o aprendizado até você, com pacotes acessíveis e flexíveis.</p>
      <a href="#">Ver opções</a>
    </div>
    <div class="card">
      <h3>Consultoria para Inclusão Digital</h3>
      <p>Para empresas ou indivíduos que desejam dar os primeiros passos no mundo digital.</p>
      <a href="#">Solicite uma consultoria</a>
    </div>
  </section>

  <section class="hero" id="sobre">
    <h2>Sobre o Infotech Soluções</h2>
    <p>Somos apaixonados por ensinar e acreditamos que todo mundo pode aprender tecnologia com leveza e confiança. Com anos de experiência em suporte técnico e didática, oferecemos um ambiente seguro e acolhedor para você evoluir.</p>
  </section>

  <section class="hero" id="contato">
    <h2>Contato</h2>
    <form action="https://formspree.io/f/xovlkglk" method="POST">
      <label>Email:
        <input type="email" name="email" required>
      </label>
      <label>Mensagem:
        <textarea name="message" required></textarea>
      </label>
      <button type="submit">Enviar</button>
    </form>
    <p>Ou entre em contato direto:<br>
      Email: <a href="mailto:ariadne.c@hotmail.com">ariadne.c@hotmail.com</a><br>
      WhatsApp: <a href="https://wa.me/5583981014221" target="_blank">(83) 98101-4221</a>
    </p>
  </section>

  <a href="https://wa.me/5583912345678" class="whatsapp-float" target="_blank">
    <img src="https://img.icons8.com/color/48/000000/whatsapp--v1.png" alt="WhatsApp" />
  </a>

  <footer>
    <p>&copy; 2025 Infotech Soluções - Todos os direitos reservados</p>
  </footer>
</body>
</html>
"""

st.markdown(html_code, unsafe_allow_html=True)
