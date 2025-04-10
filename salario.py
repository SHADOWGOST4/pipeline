def calcular_pago(tipo_contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas):

    maximo_horas = 180  # Horas máximas permitidas por mes

    # Tarifas por hora según el tipo de contrato
    tarifas = {
        "docente tiempo completo": {"diurna": 40000, "nocturna": 50000, "dominical_festivo": 60000},
        "docente medio tiempo": {"diurna": 20000, "nocturna": 25000, "dominical_festivo": 30000}
    }

    # Validar el tipo de contrato
    if tipo_contrato not in tarifas:
        return "Error: Tipo de contrato no válido."
    
    # Validar las horas trabajadas
    total_horas = horas_diurnas + horas_nocturnas + horas_dominicales + horas_festivas

    if total_horas > maximo_horas:
        return "Error: Excede el máximo de horas permitidas por mes."
    
    # Validar horas negativas
    if horas_diurnas < 0 or horas_nocturnas < 0 or horas_dominicales < 0 or horas_festivas < 0:
        return "Error: Las horas no pueden ser negativas."

    # Calcular el salario bruto
    tarifa = tarifas[tipo_contrato]
    salario_bruto = (horas_diurnas * tarifa["diurna"] +
                     horas_nocturnas * tarifa["nocturna"] +
                     (horas_dominicales + horas_festivas) * tarifa["dominical_festivo"])

    # Calcular descuentos (parafiscales: 9%)
    descuento_parafiscales = salario_bruto * 0.09
    salario_neto = salario_bruto - descuento_parafiscales

    # Retornar resultados
    return salario_neto