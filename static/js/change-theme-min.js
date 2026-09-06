document.addEventListener("DOMContentLoaded", () => {
  const themeItems = document.querySelectorAll("[data-theme]");

  const themeLabel = document.getElementById("themeLabel");

  // Verifica se o elemento existe
  if (!themeLabel) {
    console.warn("Elemento #themeLabel não encontrado.");

    return;
  }

  const themes = {
    light: {
      text: "Claro",
      icon: "bi-sun",
    },

    dark: {
      text: "Escuro",
      icon: "bi-moon",
    },

    system: {
      text: "Sistema",
      icon: "bi-circle-half",
    },
  };

  function getSystemTheme() {
    return window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  }

  function applyTheme(theme) {
    // Proteção contra valores inválidos
    if (!Object.hasOwn(themes, theme)) {
      theme = "system";
    }

    // Define o tema efetivo
    const effectiveTheme = theme === "system" ? getSystemTheme() : theme;

    // Aplica o tema ao Bootstrap 5.3
    document.documentElement.setAttribute("data-bs-theme", effectiveTheme);

    // Atualiza o botão principal
    themeLabel.innerHTML = `
            <i class="bi ${themes[theme].icon}"></i>
            ${themes[theme].text}
        `;

    // Salva a preferência
    localStorage.setItem("theme", theme);

    // Marca a opção selecionada
    themeItems.forEach((item) => {
      item.classList.toggle("active", item.dataset.theme === theme);
    });
  }

  // Recupera a preferência salva
  const savedTheme = localStorage.getItem("theme") || "system";

  // Aplica o tema inicial
  applyTheme(savedTheme);

  // Eventos dos itens do menu
  themeItems.forEach((item) => {
    item.addEventListener("click", () => {
      applyTheme(item.dataset.theme);
    });
  });

  // Detecta mudanças no tema do sistema
  const systemTheme = window.matchMedia("(prefers-color-scheme: dark)");

  systemTheme.addEventListener("change", () => {
    const currentTheme = localStorage.getItem("theme") || "system";

    // Só reage automaticamente
    // quando o usuário escolheu Sistema
    if (currentTheme === "system") {
      applyTheme("system");
    }
  });
});
