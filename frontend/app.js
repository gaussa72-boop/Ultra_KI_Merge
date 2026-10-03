const state={webSearch:true,model:'gpt-5.6-sol'};
const $=s=>document.querySelector(s);
const messages=$('#messages');
function addMessage(kind,text){const row=document.createElement('div');row.className='message '+kind;if(kind==='ai'){const img=document.createElement('img');img.src='/static/assets/ultra-orb.svg';row.appendChild(img)}const b=document.createElement('div');b.className='bubble';b.innerHTML='<small>'+(kind==='user'?'Du':'Ultra-KI')+' · '+new Date().toLocaleTimeString('de-DE',{hour:'2-digit',minute:'2-digit'})+'</small><div>'+escapeHtml(text).replace(/\n/g,'<br>')+'</div>';row.appendChild(b);messages.appendChild(row);messages.scrollTop=messages.scrollHeight}
function escapeHtml(s){return String(s).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[m]))}
async function send(){const input=$('#input'),text=input.value.trim();if(!text)return;addMessage('user',text);input.value='';try{const r=await fetch('/api/chat/send',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({user_id:1,room:'Wunderland',message:text,model:state.model,web_search:state.webSearch})});const data=await r.json();addMessage('ai',data.response||data.error||'Keine Antwort.')}catch(e){addMessage('ai','Verbindung zur Ultra-KI fehlgeschlagen. Bitte Render-Logs prüfen. '+e.message)}}
$('#composer').addEventListener('submit',e=>{e.preventDefault();send()});
$('#webSearch').addEventListener('change',e=>state.webSearch=e.target.checked);
$('#model').addEventListener('change',e=>state.model=e.target.value);
$('#webToggle').addEventListener('click',()=>{$('#webSearch').click()});
$('#newChat').addEventListener('click',()=>{messages.innerHTML='';addMessage('ai','Neuer Chat gestartet. Womit soll ich dich unterstützen?')});
$('#attachBtn').addEventListener('click',()=>$('#fileInput').click());
$('#drop').addEventListener('click',()=>$('#fileInput').click());
$('#fileInput').addEventListener('change',e=>{const names=[...e.target.files].map(f=>f.name).join(', ');if(names)addMessage('user','Datei hochgeladen: '+names)});
document.querySelectorAll('.nav').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('.nav').forEach(x=>x.classList.remove('active'));b.classList.add('active')}));
$('#themeBtn').addEventListener('click',()=>document.body.classList.toggle('light'));
