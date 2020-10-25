function debito(){
    document.getElementById("todas-transacoesid").className = "hidden";
    document.getElementById("transacoes-debitoid").className = "todas-transacoes";
    document.getElementById("transacoes-creditoid").className = "hidden";
    document.getElementById("mostrarsaldo").className = "hidden";
    document.getElementById("mostrarsaldo2").className = "hidden";
}
function todas(){
    document.getElementById("todas-transacoesid").className = "todas-transacoes";
    document.getElementById("transacoes-debitoid").className = "hidden";
    document.getElementById("transacoes-creditoid").className = "hidden";
    document.getElementById("mostrarsaldo").className = "saldo";
    document.getElementById("mostrarsaldo2").className = "saldo-bottom";
}
function credito(){
    document.getElementById("todas-transacoesid").className = "hidden";
    document.getElementById("transacoes-debitoid").className = "hidden";
    document.getElementById("transacoes-creditoid").className = "todas-transacoes";
    document.getElementById("mostrarsaldo").className = "hidden";
    document.getElementById("mostrarsaldo2").className = "hidden";
}