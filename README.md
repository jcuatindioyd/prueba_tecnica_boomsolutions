# Módulo crm_order

Este módulo agrega funcionalidad al modelo CRM.LEAD,donde se puede aprobar oportunidades.

## Estructura del Módulo

```
crm_order/
├── data/
│   └── crm_lead.xml          # Registros de ejemplo de órdenes de venta con los nuevos campos llenos.
├── i18n/
│   └── es_CO.po              # Contiene las traducciones para el idioma español (Colombia).
├── models/
│   ├── __init__.py           # Importa los archivos .py
│   └── crm_lead.py           # Contine los nuevos campos definidos en el modelo crm.lead
├── views/
│   └── crm_order_views.xml   # Contine la vista heredada de crm.lead con los nuevos campos.
├── __init__.py               # Este archivo importa los submódulos que contienen archivos .py
├── __manifest__.py           # Define el módulo
├── README.md                 #Este archivo
```

## Funcionalidades

- **Nuevos campos en modelo crm.lead**:
  - `x_lead_category`: Categoría ()
  - `x_delivery_deadline`: Plazo de entrega ()
  - `x_approved_by`: Aprobado por (Indica quién aprobó la oportunidad)
  - `x_approved_date`: Fecha de aprobación (Fecha en que se aprobó la oportunidad)
  - `x_installation_required`: Requiere instalación (Indica si la oportunidad requiere instalación técnica posterior a la venta.)
  - `x_installation_date`: Fecha de instalación (Fecha programada para la instalación del servicio o entrega técnica.)
  - `x_contract_reference`: Referencia de contrato (Código o número de referencia del contrato asociado a la oportunidad.)
  - `x_support_required`: Requiere soporte  (Indica si el cliente ha solicitado soporte técnico postventa.)
  - `x_duration_since_approved`: Duración desde aprobado (Indica el tiempo transcurrido desde que se aprobó la orden de venta.)
- **Botón Aprobar orden**: Botón que permite registrar la fecha actua y usuario que aprueba la orden.

## Pasos de Instalación

- Ingresar al módulo de Aplicaciones
- Filtrar por nombre de módulo crm_order
- Click en el boton Activar

## Como probarlo

- Ingresar al módulo CRM/Oportunidades
- Abrir un registro de oportunidad o crear uno nuevo
- Registrar los datos
- Click en el boton APROBAR ORDEN registrar la fecha actual y usuario que aprueba la orden en los campos `x_approved_by` y `x_delivery_deadline` 
- Al registrar o actualizar el campo `x_approved_date` se puede observar la actualización del campo `x_duration_since_approved` con los días transcurridos.
- Guarda y verifica que los campos se hayan actualizado en el formulario.
