document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('formAdicionarItem');
    const tabela = document.getElementById('tabelaEstoque').querySelector('tbody');

    // Adicionar item
    if (form) {
        form.addEventListener('submit', function (event) {
            event.preventDefault();

            const nome = document.getElementById('nomeItem').value;
            const desc = document.getElementById('descItem').value;
            const qtd = document.getElementById('qtdItem').value;

            const novoCodigo = tabela.rows.length + 1;

            const novaLinha = tabela.insertRow();
            novaLinha.innerHTML = `
                <td>${novoCodigo}</td>
                <td>${nome}</td>
                <td>${desc}</td>
                <td>${qtd}</td>
                <td><button class="btn btn-outline-danger btn-sm btn-remover">Remover</button></td>
            `;

            form.reset();
        });
    }

    // Remover item e reajustar o código
    if (tabela) {
        tabela.addEventListener('click', function (event) {
            if (event.target.classList.contains('btn-remover')) {
                const linha = event.target.closest('tr');
                linha.remove();

                Array.from(tabela.rows).forEach((tr, index) => {
                    tr.cells[0].innerText = index + 1;
                });
            }
        });
    }
});