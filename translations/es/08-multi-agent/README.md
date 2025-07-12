<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c692a8975d7d5b99575a553de1c5e8a7",
  "translation_date": "2025-07-12T10:50:31+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "es"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.es.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

# Patrones de diseño multiagente

En cuanto comienzas a trabajar en un proyecto que involucra múltiples agentes, necesitarás considerar el patrón de diseño multiagente. Sin embargo, puede que no sea inmediatamente claro cuándo cambiar a multiagentes y cuáles son las ventajas.

## Introducción

En esta lección, buscamos responder las siguientes preguntas:

- ¿En qué escenarios son aplicables los multiagentes?
- ¿Cuáles son las ventajas de usar multiagentes en lugar de un solo agente realizando múltiples tareas?
- ¿Cuáles son los componentes básicos para implementar el patrón de diseño multiagente?
- ¿Cómo podemos tener visibilidad de cómo los múltiples agentes interactúan entre sí?

## Objetivos de aprendizaje

Después de esta lección, deberías ser capaz de:

- Identificar escenarios donde los multiagentes son aplicables
- Reconocer las ventajas de usar multiagentes frente a un agente singular.
- Comprender los componentes básicos para implementar el patrón de diseño multiagente.

¿Cuál es la idea general?

*Los multiagentes son un patrón de diseño que permite que varios agentes trabajen juntos para lograr un objetivo común*.

Este patrón se usa ampliamente en diversos campos, incluyendo robótica, sistemas autónomos y computación distribuida.

## Escenarios donde los multiagentes son aplicables

Entonces, ¿en qué escenarios es conveniente usar multiagentes? La respuesta es que hay muchos casos donde emplear múltiples agentes es beneficioso, especialmente en los siguientes:

- **Grandes cargas de trabajo**: Las grandes cargas pueden dividirse en tareas más pequeñas y asignarse a diferentes agentes, permitiendo procesamiento paralelo y una finalización más rápida. Un ejemplo es una tarea de procesamiento de datos a gran escala.
- **Tareas complejas**: Las tareas complejas, al igual que las grandes cargas, pueden descomponerse en subtareas más pequeñas y asignarse a diferentes agentes, cada uno especializado en un aspecto específico. Un buen ejemplo es en vehículos autónomos, donde distintos agentes gestionan la navegación, detección de obstáculos y comunicación con otros vehículos.
- **Diversidad de especialización**: Diferentes agentes pueden tener especializaciones diversas, permitiéndoles manejar distintos aspectos de una tarea de manera más efectiva que un solo agente. Un buen ejemplo es en el sector salud, donde agentes pueden encargarse de diagnósticos, planes de tratamiento y monitoreo de pacientes.

## Ventajas de usar multiagentes frente a un agente singular

Un sistema con un solo agente puede funcionar bien para tareas simples, pero para tareas más complejas, usar múltiples agentes ofrece varias ventajas:

- **Especialización**: Cada agente puede especializarse en una tarea específica. La falta de especialización en un solo agente significa que puede hacer de todo, pero confundirse ante tareas complejas, terminando por realizar tareas para las que no está mejor capacitado.
- **Escalabilidad**: Es más fácil escalar sistemas añadiendo más agentes que sobrecargando un solo agente.
- **Tolerancia a fallos**: Si un agente falla, otros pueden continuar funcionando, asegurando la fiabilidad del sistema.

Veamos un ejemplo: reservar un viaje para un usuario. Un sistema con un solo agente tendría que manejar todos los aspectos del proceso, desde buscar vuelos hasta reservar hoteles y autos de alquiler. Para lograr esto, el agente necesitaría herramientas para todas estas tareas, lo que podría resultar en un sistema complejo y monolítico, difícil de mantener y escalar. Un sistema multiagente, en cambio, podría tener agentes especializados en buscar vuelos, reservar hoteles y autos de alquiler. Esto haría el sistema más modular, fácil de mantener y escalable.

Compáralo con una agencia de viajes familiar frente a una agencia de viajes franquiciada. La agencia familiar tendría un solo agente manejando todo el proceso, mientras que la franquicia tendría diferentes agentes para cada aspecto del proceso.

## Componentes básicos para implementar el patrón de diseño multiagente

Antes de implementar el patrón multiagente, necesitas entender los componentes que lo conforman.

Volviendo al ejemplo de reservar un viaje para un usuario, los componentes básicos incluirían:

- **Comunicación entre agentes**: Los agentes encargados de buscar vuelos, reservar hoteles y autos deben comunicarse y compartir información sobre las preferencias y restricciones del usuario. Debes decidir los protocolos y métodos para esta comunicación. Concretamente, el agente de vuelos debe comunicarse con el de hoteles para asegurar que la reserva del hotel coincida con las fechas del vuelo. Esto implica que los agentes deben compartir información sobre las fechas de viaje del usuario, por lo que debes decidir *qué agentes comparten información y cómo lo hacen*.
- **Mecanismos de coordinación**: Los agentes deben coordinar sus acciones para cumplir con las preferencias y restricciones del usuario. Por ejemplo, una preferencia podría ser que el hotel esté cerca del aeropuerto, mientras que una restricción podría ser que los autos de alquiler solo estén disponibles en el aeropuerto. Esto significa que el agente de hoteles debe coordinarse con el de autos para cumplir con estas condiciones. Debes decidir *cómo los agentes coordinan sus acciones*.
- **Arquitectura del agente**: Los agentes deben tener una estructura interna para tomar decisiones y aprender de sus interacciones con el usuario. Por ejemplo, el agente de vuelos debe poder decidir qué vuelos recomendar. Debes decidir *cómo los agentes toman decisiones y aprenden de sus interacciones*. Un ejemplo podría ser que el agente de vuelos use un modelo de aprendizaje automático para recomendar vuelos basados en preferencias pasadas.
- **Visibilidad de las interacciones multiagente**: Necesitas tener visibilidad de cómo los agentes interactúan entre sí. Esto implica contar con herramientas y técnicas para rastrear actividades e interacciones, como herramientas de registro y monitoreo, visualización y métricas de rendimiento.
- **Patrones multiagente**: Existen diferentes patrones para implementar sistemas multiagente, como arquitecturas centralizadas, descentralizadas e híbridas. Debes elegir el patrón que mejor se adapte a tu caso.
- **Humano en el ciclo**: En la mayoría de los casos, habrá un humano en el ciclo y debes indicar a los agentes cuándo solicitar intervención humana. Esto puede ser, por ejemplo, cuando un usuario pide un hotel o vuelo específico que los agentes no han recomendado, o cuando se requiere confirmación antes de reservar.

## Visibilidad de las interacciones multiagente

Es importante tener visibilidad de cómo los múltiples agentes interactúan entre sí. Esta visibilidad es esencial para depurar, optimizar y asegurar la efectividad general del sistema. Para lograrlo, necesitas herramientas y técnicas para rastrear actividades e interacciones de los agentes. Esto puede incluir herramientas de registro y monitoreo, visualización y métricas de rendimiento.

Por ejemplo, en el caso de reservar un viaje, podrías tener un panel que muestre el estado de cada agente, las preferencias y restricciones del usuario, y las interacciones entre agentes. Este panel podría mostrar las fechas de viaje, los vuelos recomendados por el agente de vuelos, los hoteles recomendados por el agente de hoteles y los autos recomendados por el agente de alquiler. Esto te daría una visión clara de cómo interactúan los agentes y si se están cumpliendo las preferencias y restricciones del usuario.

Veamos cada aspecto con más detalle.

- **Herramientas de registro y monitoreo**: Quieres registrar cada acción que realiza un agente. Una entrada de registro podría almacenar información sobre el agente que realizó la acción, la acción tomada, el momento en que se realizó y el resultado. Esta información puede usarse para depurar, optimizar y más.
- **Herramientas de visualización**: Las herramientas de visualización te ayudan a ver las interacciones entre agentes de forma más intuitiva. Por ejemplo, podrías tener un gráfico que muestre el flujo de información entre agentes. Esto puede ayudarte a identificar cuellos de botella, ineficiencias y otros problemas.
- **Métricas de rendimiento**: Las métricas te ayudan a seguir la efectividad del sistema multiagente. Por ejemplo, podrías medir el tiempo para completar una tarea, la cantidad de tareas completadas por unidad de tiempo y la precisión de las recomendaciones de los agentes. Esta información ayuda a identificar áreas de mejora y optimizar el sistema.

## Patrones multiagente

Vamos a explorar algunos patrones concretos que podemos usar para crear aplicaciones multiagente. Aquí algunos patrones interesantes a considerar:

### Chat grupal

Este patrón es útil cuando quieres crear una aplicación de chat grupal donde múltiples agentes puedan comunicarse entre sí. Usos típicos incluyen colaboración en equipo, soporte al cliente y redes sociales.

En este patrón, cada agente representa a un usuario en el chat grupal, y los mensajes se intercambian entre agentes usando un protocolo de mensajería. Los agentes pueden enviar mensajes al grupo, recibir mensajes y responder a otros agentes.

Este patrón puede implementarse con una arquitectura centralizada, donde todos los mensajes pasan por un servidor central, o una arquitectura descentralizada, donde los mensajes se intercambian directamente.

![Group chat](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.es.png)

### Transferencia de tareas

Este patrón es útil cuando quieres crear una aplicación donde múltiples agentes puedan transferirse tareas entre sí.

Usos típicos incluyen soporte al cliente, gestión de tareas y automatización de flujos de trabajo.

En este patrón, cada agente representa una tarea o un paso en un flujo de trabajo, y los agentes pueden transferir tareas a otros agentes según reglas predefinidas.

![Hand off](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.es.png)

### Filtrado colaborativo

Este patrón es útil cuando quieres crear una aplicación donde múltiples agentes colaboren para hacer recomendaciones a los usuarios.

La razón para que varios agentes colaboren es que cada uno puede tener diferentes especializaciones y contribuir al proceso de recomendación de distintas maneras.

Por ejemplo, un usuario quiere una recomendación sobre la mejor acción para comprar en el mercado bursátil.

- **Experto en la industria**: Un agente podría ser experto en una industria específica.
- **Análisis técnico**: Otro agente podría ser experto en análisis técnico.
- **Análisis fundamental**: Otro agente podría ser experto en análisis fundamental. Al colaborar, estos agentes pueden ofrecer una recomendación más completa al usuario.

![Recommendation](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.es.png)

## Escenario: proceso de reembolso

Considera un escenario donde un cliente intenta obtener un reembolso por un producto. Pueden estar involucrados varios agentes, pero dividiremos entre agentes específicos para este proceso y agentes generales que pueden usarse en otros procesos.

**Agentes específicos para el proceso de reembolso**:

Algunos agentes que podrían estar involucrados en el proceso de reembolso:

- **Agente del cliente**: Representa al cliente y es responsable de iniciar el proceso de reembolso.
- **Agente del vendedor**: Representa al vendedor y es responsable de procesar el reembolso.
- **Agente de pago**: Representa el proceso de pago y es responsable de reembolsar el pago al cliente.
- **Agente de resolución**: Representa el proceso de resolución y se encarga de resolver cualquier problema que surja durante el reembolso.
- **Agente de cumplimiento**: Representa el proceso de cumplimiento y asegura que el proceso de reembolso cumpla con regulaciones y políticas.

**Agentes generales**:

Estos agentes pueden usarse en otras áreas de tu negocio.

- **Agente de envíos**: Representa el proceso de envío y es responsable de enviar el producto de vuelta al vendedor. Puede usarse tanto para reembolsos como para envíos generales de productos por compras.
- **Agente de retroalimentación**: Representa el proceso de recolección de opiniones del cliente. La retroalimentación puede darse en cualquier momento, no solo durante el reembolso.
- **Agente de escalamiento**: Representa el proceso de escalamiento y se encarga de elevar problemas a un nivel superior de soporte. Puedes usar este agente en cualquier proceso que requiera escalamiento.
- **Agente de notificaciones**: Representa el proceso de notificaciones y es responsable de enviar avisos al cliente en distintas etapas del reembolso.
- **Agente de análisis**: Representa el proceso de análisis y se encarga de analizar datos relacionados con el reembolso.
- **Agente de auditoría**: Representa el proceso de auditoría y asegura que el proceso de reembolso se realice correctamente.
- **Agente de reportes**: Representa el proceso de generación de informes sobre el reembolso.
- **Agente de conocimiento**: Representa el proceso de gestión del conocimiento y mantiene una base de datos con información relacionada con el reembolso. Este agente puede tener conocimiento tanto de reembolsos como de otras áreas del negocio.
- **Agente de seguridad**: Representa el proceso de seguridad y asegura la protección del proceso de reembolso.
- **Agente de calidad**: Representa el proceso de calidad y asegura la calidad del proceso de reembolso.

Hay bastantes agentes listados, tanto para el proceso específico de reembolso como para los agentes generales que pueden usarse en otras áreas de tu negocio. Esperamos que esto te dé una idea de cómo decidir qué agentes usar en tu sistema multiagente.

## Tarea
## Lección Anterior

[Planificación del Diseño](../07-planning-design/README.md)

## Próxima Lección

[Metacognición en Agentes de IA](../09-metacognition/README.md)

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.