document.addEventListener("DOMContentLoaded", () => {

    // =========================================
    // PÁGINA CARREGADA
    // =========================================

    document.body.classList.add("pagina-carregada");


    // =========================================
    // ANIMAÇÃO DOS BOTÕES
    // =========================================

    const botoes = document.querySelectorAll(
        ".btn-principal, .btn-secundario, .dashboard-button, button"
    );

    botoes.forEach(botao => {

        botao.addEventListener("click", function () {

            this.classList.add("clicando");

            setTimeout(() => {
                this.classList.remove("clicando");
            }, 180);

        });

    });


    // =========================================
    // ANIMAÇÃO DOS RECURSOS DA HOME
    // =========================================

    const recursos = document.querySelectorAll(
        ".recurso-inicio"
    );

    recursos.forEach((recurso, index) => {

        recurso.style.animationDelay =
            `${index * 0.12}s`;

        recurso.classList.add("recurso-animado");

    });


    // =========================================
    // ANIMAÇÃO DAS TAREFAS DE EXEMPLO
    // =========================================

    const tarefasExemplo = document.querySelectorAll(
        ".tarefa-demo"
    );

    tarefasExemplo.forEach((tarefa, index) => {

        tarefa.style.animationDelay =
            `${0.25 + index * 0.12}s`;

        tarefa.classList.add("tarefa-animada");

    });


    // =========================================
    // TAREFAS DA PRIMEIRA TELA
    // =========================================

    tarefasExemplo.forEach(tarefa => {

        tarefa.addEventListener("click", () => {

            const check = tarefa.querySelector(
                ".check-demo"
            );

            if (!check) return;


            if (check.classList.contains("marcado")) {

                check.classList.remove("marcado");

                check.textContent = "";

                tarefa.classList.remove(
                    "concluida-demo"
                );

            } else {

                check.classList.add("marcado");

                check.textContent = "✓";

                tarefa.classList.add(
                    "concluida-demo"
                );

            }

        });

    });


    // =========================================
    // CAMPOS INTERATIVOS
    // =========================================

    const campos = document.querySelectorAll(
        ".campo input, .campo textarea, .campo select"
    );

    campos.forEach(campo => {

        campo.addEventListener("focus", () => {

            if (campo.parentElement) {
                campo.parentElement.classList.add(
                    "campo-focado"
                );
            }

        });


        campo.addEventListener("blur", () => {

            if (campo.parentElement) {
                campo.parentElement.classList.remove(
                    "campo-focado"
                );
            }

        });

    });


    // =========================================
    // MOSTRAR / OCULTAR SENHA
    // =========================================

    const camposSenha = document.querySelectorAll(
        'input[type="password"]'
    );

    camposSenha.forEach(campo => {

        const container = campo.parentElement;

        if (!container) return;


        const botaoSenha = document.createElement(
            "button"
        );

        botaoSenha.type = "button";

        botaoSenha.className = "btn-senha";

        botaoSenha.textContent = "Mostrar senha";


        botaoSenha.addEventListener("click", () => {

            if (campo.type === "password") {

                campo.type = "text";

                botaoSenha.textContent =
                    "Ocultar senha";

            } else {

                campo.type = "password";

                botaoSenha.textContent =
                    "Mostrar senha";

            }

        });


        container.appendChild(botaoSenha);

    });


    // =========================================
    // FOCO AUTOMÁTICO
    // =========================================

    const primeiroCampo = document.querySelector(
        ".auth-card input"
    );

    if (primeiroCampo) {

        setTimeout(() => {
            primeiroCampo.focus();
        }, 400);

    }


    // =========================================
    // CONFIRMAR SAÍDA
    // =========================================

    const botoesLogout = document.querySelectorAll(
        'a[href*="logout"]'
    );

    botoesLogout.forEach(botao => {

        botao.addEventListener("click", event => {

            const confirmar = confirm(
                "Deseja realmente sair da sua conta?"
            );

            if (!confirmar) {
                event.preventDefault();
            }

        });

    });


    // =========================================
    // CONFIRMAR EXCLUSÃO
    // =========================================

    const formulariosExcluir =
        document.querySelectorAll(
            ".tarefa-acoes form"
        );

    formulariosExcluir.forEach(formulario => {

        formulario.addEventListener(
            "submit",
            event => {

                const confirmar = confirm(
                    "Tem certeza que deseja excluir esta tarefa?"
                );

                if (!confirmar) {
                    event.preventDefault();
                }

            }
        );

    });


    // =========================================
    // FORMULÁRIOS
    // =========================================

    const formularios =
        document.querySelectorAll("form");

    formularios.forEach(formulario => {

        formulario.addEventListener(
            "submit",
            () => {

                const botao =
                    formulario.querySelector(
                        'button[type="submit"]'
                    );

                if (!botao) return;


                // Não altera botão de exclusão
                if (
                    formulario.closest(
                        ".tarefa-acoes"
                    )
                ) {
                    return;
                }


                botao.disabled = true;

                botao.classList.add(
                    "processando"
                );

                botao.textContent =
                    "Processando...";

            }
        );

    });


    // =========================================
    // ANIMAÇÃO DAS TAREFAS CADASTRADAS
    // =========================================

    const tarefas =
        document.querySelectorAll(".tarefa");

    tarefas.forEach((tarefa, index) => {

        tarefa.style.animationDelay =
            `${index * 0.08}s`;

        tarefa.classList.add("tarefa-real");

    });


    // =========================================
    // TÍTULO DA LISTA
    // =========================================

    const tituloLista =
        document.querySelector(".lista-titulo");

    if (tituloLista) {

        const observer =
            new IntersectionObserver(
                entradas => {

                    entradas.forEach(entrada => {

                        if (
                            entrada.isIntersecting
                        ) {

                            entrada.target.classList.add(
                                "titulo-visivel"
                            );

                        }

                    });

                },
                {
                    threshold: 0.2
                }
            );

        observer.observe(tituloLista);

    }

});