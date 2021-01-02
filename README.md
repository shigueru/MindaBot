# MindaBot

## Descripción gereral

**MindaBot** es un bot de Telegram implementado en Python. Su función es enviar datos del video que se envió antes desde un cliente de telegram de escritorio. La idea original era tambien implementar el envio del video mediante el bot. Pero debido a las limitaciones impuestas sobre el tamaño del video que puede enviar un bot, no fue posible .Los datos son los siguientes:

* Nombre
* Canal 
* Fecha
* Dia
* Mes
* Año
* Etapa
* Estado

Los datos iran acompañados de un hashtag (#) que permita una busqueda mas eficiente en Telegram.

## Descripción de los datos

Los datos que se envian en la descripción que acompaña a un video tienen el siguiente significado.

### Nombre

Este es el nombre del video. Se obtiene del nombre que se le da al video en la plataforma de Youtube. Este nombre puede contener caracteres especiales propios del idioma del youtuber.

### Canal

Este es el nombre del canal de Youtube desde se encuentra subido el video.

### Fecha

Esta es la fecha de publicación del video en la plataforma de Youtube. La fecha tiene el siguiente formato.

dd-mm-aa (dia-mes-año) incluyendo los guiones.

Los datos de dia, mes y año son los mismos. Estos se consideran para poder tener una alternativa de busqueda que permita ser mas general por año, mes o dia.

### Etapa

Este puede tener dos valores especificos en este momento. Los cuales son:

* tailandia
* japon

Las opciones hacen referencia al momento de desarrollo profesional del youtuber. El cual se mide por su grado de internacionalización.

### Estado

Este dato solo puede tener dos valores. Los cuales son:

* copia
* original

Las opciones se refieren al estado del video en la plataforma. Es decir, si el video fue publicado en un canal oficial se considera un estado *original*. En el caso de que el video se encuentre borrado o puesto en privado, se realizara una busqueda por la plataforma de Youtube. Si se logra ubicar el video en otro canal que no tenga los derechos o permisos requeridos tendra un estado *copia*.