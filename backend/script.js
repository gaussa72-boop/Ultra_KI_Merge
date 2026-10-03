const products=[
{id:1,name:"Noir Élégance",cat:"Herren",price:79.90,img:"images/parfum-01.jpg",desc:"Warme Hölzer, Gewürze und Amber."},
{id:2,name:"Lumière",cat:"Damen",price:89.90,img:"images/parfum-02.jpg",desc:"Jasmin, Iris und sanfter Moschus."},
{id:3,name:"Éclat",cat:"Unisex",price:94.90,img:"images/parfum-03.jpg",desc:"Zitrus, aromatische Hölzer und Amber."},
{id:4,name:"Velours",cat:"Unisex",price:99.90,img:"images/parfum-04.jpg",desc:"Vanille, Tonka und cremiges Sandelholz."}];
let cart=JSON.parse(localStorage.getItem("aurelis")||"[]"),selected=null,config={};
const euro=n=>n.toLocaleString("de-DE",{style:"currency",currency:"EUR"});
const fallback="images/placeholder.svg";
function save(){localStorage.setItem("aurelis",JSON.stringify(cart));renderCart()}
function render(){let f=document.querySelector("#filter").value;productsEl.innerHTML=products.filter(p=>f==="all"||p.cat===f).map(p=>`<article class="product"><div class="pic"><img src="${p.img}" onerror="this.src='${fallback}'"></div><div class="pi"><span class="eyebrow">${p.cat}</span><h3>${p.name}</h3><p>${p.desc}</p><b>${euro(p.price)}</b><button class="btn full" onclick="detail(${p.id})">Details</button></div></article>`).join("")}
function renderCart(){cartCount.textContent=cart.reduce((a,x)=>a+x.qty,0);cartItems.innerHTML=cart.length?cart.map(x=>`<div class="row"><img src="${x.img}" onerror="this.src='${fallback}'"><div><h4>${x.name}</h4><b>${euro(x.price*x.qty)}</b><div><button onclick="qty(${x.id},-1)">−</button> ${x.qty} <button onclick="qty(${x.id},1)">+</button></div></div><button onclick="removeItem(${x.id})">×</button></div>`).join(""):"<p>Dein Warenkorb ist leer.</p>";total.textContent=euro(cart.reduce((a,x)=>a+x.price*x.qty,0))}
function qty(id,n){let x=cart.find(x=>x.id===id);if(!x)return;x.qty+=n;if(x.qty<1)removeItem(id);else save()} function removeItem(id){cart=cart.filter(x=>x.id!==id);save()}
function add(id){let p=products.find(x=>x.id===id),x=cart.find(x=>x.id===id);x?x.qty++:cart.push({...p,qty:1});save();openCart()}
function detail(id){selected=products.find(x=>x.id===id);mimg.src=selected.img;mimg.onerror=()=>mimg.src=fallback;mcat.textContent=selected.cat;mname.textContent=selected.name;mdesc.textContent=selected.desc;mprice.textContent=euro(selected.price);modal.classList.add("open")}
function openCart(){cartEl.classList.add("open");shade.classList.add("open")}function closeCart(){cartEl.classList.remove("open");shade.classList.remove("open")}
const productsEl=document.querySelector("#products"),cartEl=document.querySelector("#cart");
openCartBtn=document.querySelector("#openCart");openCartBtn.onclick=openCart;closeCartBtn=document.querySelector("#closeCart");closeCartBtn.onclick=closeCart;shade.onclick=closeCart;
document.querySelector("#filter").onchange=render;document.querySelector("#closeModal").onclick=()=>modal.classList.remove("open");document.querySelector("#madd").onclick=()=>{add(selected.id);modal.classList.remove("open")};
document.querySelector("#checkout").onclick=async()=>{if(!cart.length)return alert("Warenkorb ist leer.");let email=prompt("E-Mail für die Zahlungsbestätigung:");if(!email)return;let r=await fetch("/api/create-checkout-session",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({items:cart,customer:{email}})});let d=await r.json();if(d.url)location.href=d.url;else alert(d.error||"Checkout konnte nicht erstellt werden.")};
document.querySelector("#wa").onclick=()=>location.href=`https://wa.me/${config.whatsappNumber}?text=${encodeURIComponent("Hallo AURELIS, ich habe eine Frage zu euren Parfums.")}`;
document.querySelector("#tg").onclick=()=>location.href=`https://t.me/${config.telegramUsername}`;
document.querySelector("#whatsOrder").onclick=()=>{if(!cart.length)return alert("Warenkorb ist leer.");let t="Hallo AURELIS, ich möchte bestellen:%0A"+cart.map(x=>`${x.name} x${x.qty} – ${euro(x.price*x.qty)}`).join("%0A")+`%0A%0AGesamt: ${total.textContent}`;window.open(`https://wa.me/${config.whatsappNumber}?text=${t}`,"_blank")};
fetch("/api/config").then(r=>r.json()).then(c=>{config=c;render();renderCart()}).catch(()=>{render();renderCart()});