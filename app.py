
from flask import Flask, render_template, request, send_file
from docx import Document
import os

app = Flask(__name__)

def generate_docx(template_path, substitutions):
    doc = Document(template_path)
    
    for para in doc.paragraphs:
        for key, value in substitutions.items():
            if key in para.text:
                para.text = para.text.replace(key, value)
    
    output_path = "output.docx"
    doc.save(output_path)
    return output_path

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        currentDate = request.form['currentDate']
        court = request.form['court']
        place = request.form['place']
        state = request.form['state']
        section = request.form['section']
        policestation = request.form['policestation']
        fir = request.form['fir']
        date = request.form['date']
        petitioner = request.form['petitioner']
        pfather = request.form['pfather']
        page = request.form['page']
        poccupation = request.form['poccupation']
        paddress = request.form['paddress']
        business = request.form['business']
        details = request.form['details']
        respondent = request.form['respondent']
        rfather = request.form['rfather']
        rage = request.form['rage']
        roccupation = request.form['roccupation']
        raddress = request.form['raddress']
        counsel = request.form['counsel']


        # Substitution dictionary
        substitutions = {
            '{currentDate}': currentDate,
            '{court}': court,
            '{place}': place,
            '{state}': state,
            '{section}': section,
            '{policestation}': policestation,
            '{fir}': fir,
            '{date}': date,
            '{petitioner}': petitioner,
            '{pfather}': pfather,
            '{page}': page,
            '{poccupation}': poccupation,
            '{paddress}': paddress,
            '{business}': business,
            '{details}': details,
            '{respondent}': respondent,
            '{rfather}': rfather,
            '{rage}': rage,
            '{roccupation}': roccupation,
            '{raddress}': raddress,
            '{counsel}': counsel
        }

        # Generate the Word document with substituted values
        doc_path = generate_docx('template.docx', substitutions)

        # Send the generated document to the user
        return send_file(doc_path, as_attachment=True)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
