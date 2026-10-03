import "dotenv/config";
import express from "express";
import Stripe from "stripe";
import path from "path";
import { fileURLToPath } from "url";

const app = express();
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const port = process.env.PORT || 3000;
const stripe = process.env.STRIPE_SECRET_KEY?.startsWith("sk_")
  ? new Stripe(process.env.STRIPE_SECRET_KEY) : null;

app.use(express.json({limit:"100kb"}));
app.use(express.static(path.join(__dirname,"public")));

app.post("/api/create-checkout-session", async (req,res)=>{
  try {
    if (!stripe) return res.status(503).json({error:"Stripe ist noch nicht konfiguriert. Trage STRIPE_SECRET_KEY in .env ein."});
    const {items=[], customer={}} = req.body;
    if (!Array.isArray(items) || !items.length) return res.status(400).json({error:"Warenkorb ist leer."});
    const catalog = {
      "1":{name:"Noir Élégance",price:7990,image:"/images/parfum-01.jpg"},
      "2":{name:"Lumière",price:8990,image:"/images/parfum-02.jpg"},
      "3":{name:"Éclat",price:9490,image:"/images/parfum-03.jpg"},
      "4":{name:"Velours",price:9990,image:"/images/parfum-04.jpg"}
    };
    const line_items = items.map(i=>{
      const p=catalog[String(i.id)], qty=Math.max(1,Math.min(20,Number(i.qty)||1));
      if(!p) throw new Error("Unbekanntes Produkt.");
      return {quantity:qty,price_data:{currency:process.env.CURRENCY||"eur",unit_amount:p.price,product_data:{name:p.name}}};
    });
    const session=await stripe.checkout.sessions.create({
      mode:"payment",line_items,
      customer_email:customer.email||undefined,
      billing_address_collection:"required",
      shipping_address_collection:{allowed_countries:["DE","AT","CH"]},
      success_url:`${process.env.BASE_URL}/success.html?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url:`${process.env.BASE_URL}/?checkout=cancelled`,
      metadata:{customer_name:String(customer.name||"").slice(0,100)}
    });
    res.json({url:session.url});
  } catch(e){res.status(400).json({error:e.message});}
});

app.get("/api/config",(req,res)=>res.json({
  whatsappNumber:process.env.WHATSAPP_NUMBER||"",
  telegramUsername:process.env.TELEGRAM_USERNAME||"",
  shopName:process.env.SHOP_NAME||"AURELIS"
}));
app.listen(port,()=>console.log(`AURELIS läuft auf http://localhost:${port}`));