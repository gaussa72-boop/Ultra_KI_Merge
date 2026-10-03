# AURELIS Parfum Shop Pro

## Start
1. Node.js installieren.
2. `npm install`
3. `.env.example` nach `.env` kopieren.
4. WhatsApp-Nummer und Telegram-Username eintragen.
5. Für echte Kartenzahlungen einen Stripe Secret Key eintragen.
6. `npm start`
7. Shop auf `http://localhost:3000` öffnen.

## Bilder
Lege deine eigenen Dateien in `public/images/`:
- hero.jpg
- parfum-01.jpg
- parfum-02.jpg
- parfum-03.jpg
- parfum-04.jpg

## Produkte
Produkte und Preise stehen aktuell in `public/script.js` und zusätzlich serverseitig in `server.js`. Bei Änderungen müssen beide Kataloge synchron gehalten werden.

## Echte Bestellungen
Für einen produktiven Shop sollte zusätzlich ein Backend mit Datenbank, Stripe-Webhooks, Bestellstatus, E-Mail-Versand, Rechnungen und Admin-Login ergänzt werden. Niemals geheime Stripe-Schlüssel in JavaScript im `public`-Ordner speichern.

## Rechtliches
Impressum, Datenschutz, AGB und Widerrufsseite sind nur Platzhalter. Vor dem echten Verkauf müssen sie mit deinen tatsächlichen Unternehmens-/Kontaktangaben und den für deinen Shop geltenden rechtlichen Informationen ergänzt werden.
