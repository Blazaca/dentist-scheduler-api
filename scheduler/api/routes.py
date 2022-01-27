from flask import Blueprint, request, jsonify, Response, send_file
from scheduler.models import db, preset_schema, presets_schema, PresetSchema, Preset
from pathlib import Path
api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'some_value': 'Yes this link worked'}

@api.route('/appointments', methods=['POST'])
def create_preset():
    print(request.json)
    print(type(request.json))
    First_Name = request.json['First_Name']
    Last_Name = request.json['Last_Name']
    Phone_No = request.json['Phone_No']
    Email = request.json['Email']
    Subject = request.json['Subject']
    Date = request.json['Date']
    StartTime = request.json['StartTime']
    EndTime = request.json['EndTime']
    
    preset = Preset(First_Name, Last_Name, Phone_No, Email, Subject, Date, StartTime, EndTime)

    db.session.add(preset)
    db.session.commit()
    
    return {"Message": "Success, appointment created."}, 201


@api.route('/appointments', methods=['GET'])
def get_presets():
    presets = Preset.query.all()
    response = presets_schema.dump(presets)


    def formatJson(input_list):
        counter = 0
        functionDef = ['StartTime', 'EndTime']
        with open('scheduler\json_output.json', 'w+') as f:
            f.write('[\n')
            for item in input_list:
                f.write('   {\n')
                for key, val in item.items():
                    if key in functionDef:
                        f.write(f'      {key}: {val},\n')
                    elif key == 'id':
                        f.write(f'      {key}: {val}\n')
                    else:
                        f.write(f"      {key}: '{val}',\n")
                if counter != len(input_list):
                    f.write('   },\n')
                else:
                    f.write('   }]')
    
    return jsonify(response)
        


    # nilVal = ['CustomStyle', 'Description', 'EndTimeZone', 'Priority',
    # 'RecurrenceEndDate', 'RecurrenceStartDate', 'RecurrenceType', 'RecurrenceTypeCount',
    # 'Reminder','StartTimeZone', 'Description']
    # def convert_to_xml(input_list):
    #     with open('scheduler\output_file.xml', 'w+') as f:
    #         f.write('<ArrayOfDefaultSchedule xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/EJServices.Models">\n')
    #         for item in input_list:
    #             f.write('<DefaultSchedule>\n')
    #             for key, val in item.items():
    #                 if key in nilVal:
    #                     f.write(f'    <{key} i:nil="{val}" />\n')
    #                 elif key == 'id':
    #                     continue
    #                 else:
    #                     f.write(f"    <{key}>{val}</{key}>\n")
    #             f.write('</DefaultSchedule>')
    #         f.write('</ArrayOfDefaultSchedule>')

    # convert_to_xml(response)
    # convertedXML = ('output_file.xml')
    # return send_file(convertedXML, mimetype='text/xml')

@api.route('/appointments/<id>', methods = ['GET'])
def get_preset(id):
    preset = Preset.query.get(id)
    response = preset_schema.dump(preset)
    return jsonify(response)

@api.route('/appointments/<id>', methods = ['POST', 'PUT'])
def update_preset(id):
    preset = Preset.query.get(id)
    if preset:   
        preset.First_Name = request.json['First_Name']
        preset.Last_Name = request.json['Last_Name']
        preset.Phone_No = request.json['Phone_No']
        preset.Email = request.json['Email']
        preset.Subject = request.json['Subject']
        preset.Date = request.json['Date']
        preset.StartTime = request.json['StartTime']
        preset.EndTime = request.json['EndTime']
        db.session.commit()

        response = preset_schema.dump(preset)
        return jsonify(response)
    else:
        return jsonify({'Error': 'That preset id does not exist'})

@api.route('/appointments/<id>', methods = ['DELETE'])
def delete_preset(id):
    preset = Preset.query.get(id)
    print(preset)
    if preset:
        db.session.delete(preset)
        db.session.commit()

        return jsonify({'Success': f'Preset ID: {preset.id} has been deleted'})
    else:
        return jsonify({'Error': 'That preset id does not exist'})
