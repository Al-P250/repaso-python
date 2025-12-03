diccionario={
    "botella":"recipiente donde se almacenan líquidos",
    "pantalla":"dispositivo de emisión de imágenes"
}

alumno={
    "dni":"50512300A",
    "nombre":"Paco",
    "apellido": "Pérez",
    "edad":23,
    "notas":{
        "SGE":10,
        "PSP":4
    },
    "asignaturas":["SGE", "PSP"]
}

clase={
    "aula":"S-1",
    "ordenadores":[
        {"cpu":"Intel core-i5 12600",
         "hostName": "EPSUM-S3-01"},
        {"cpu":"AMD Ryzen 5 5600",
         "hostName": "EPSUM-S3-02"}
    ]
}

print(f"Aula {clase["aula"]}")
cont=1
for ordenador in clase["ordenadores"]:
  for k,v in ordenador.items():
      print(f"{k}: {v}")