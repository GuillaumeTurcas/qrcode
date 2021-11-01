import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def create_pdf():
    doc = SimpleDocTemplate("form_letter.pdf", pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)

    Story = []
    logo = "qr.png"

    im = Image(logo, 2*inch, 2*inch)
    Story.append(im)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    ncommand = input("Numéro de commande : ")
    dateevent = input("Date de l'évenement : ")
    location = input("Localisation de l'évènement : ")
    nvent = input("Nom de l'évenment : ")
    surname = input("Votre nom : ")
    name = input("Votre prénom : ")

    ptext = f"Numéro de commande : {ncommand}"
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    ptext = f"{name} {surname}"
    Story.append(Paragraph(ptext, styles["Normal"]))

    Story.append(Spacer(1, 12))
    ptext = f"Date de réservation : {time.strftime('%D', time.localtime())}"
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    ptext = f"Localisation : {location}"
    Story.append(Paragraph(ptext, styles["Normal"]))

    ptext = f"Votre commande pour {nvent} qui aura lieu le {dateevent} {location} a bien été pris en compte. Ceci est votre billet pour l'événement. Les détenteurs de billets doivent présenter leurs billets à l'entrée, de l'une des manières suivantes. Vous pouvez imprimer le billet ou présenter la version numérique du billet. Vous trouverez tous les détails de cet événement sur notre site. En cas de question ou problème, et pour toute question relative à un remboursement, veuillez contacter l'organisateur de l'événement. Si vous ne pouvez pas assister à l'événement, veuillez nous contacter. Nous nous réjouissons de vous y voir !"

    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 48))
    ptext = 'La Joute de Vinci'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    doc.build(Story)
