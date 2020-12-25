# MindaBot

## Descripción gereral

**MindaBot** es un bot de Telegram implementado en Python. Su función es enviar un video alojado en una computadora (en un entorno local) hacia un canal de Telegram. Junto con el video se envia una descripción con los siguientes datos.

* Nombre
* Canal 
* Fecha
* Etapa
* Estado

Los datos iran acompañados de un hashtag que permita una busqueda mas eficiente en Telegram.

## Descripción de los datos

Los datos que se envian en la descripción que acompaña a un video tienen el siguiente significado.

### Nombre

Este es el nombre del video. Se obtiene del nombre que se le da al video en la plataforma de Youtube. Este nombre puede contener caracteres especiales propios del idioma del youtuber.

### Canal

Este es el nombre del canal de Youtube desde se encuentra subido el video.

### Fecha

Esta es la fecha de publicación del video en la plataforma de Youtube. La fecha tiene el siguiente formato.

dd-mm-aa (dia-mes-año) incluyendo los guiones.

### Etapa

Este puede tener dos valores especificos en este momento. Los cuales son:

* Tailandia
* Japon

Las opciones hacen referencia al momento de desarrollo profesional del youtuber. El cual se mide por su grado de internacionalización.

### Estado

Este dato solo puede tener dos valores. Los cuales son:

* Copia
* Original

Las opciones se refieren al estado del video en la plataforma. Es decir, si el video fue publicado en un canal oficial se considera un estado *original*. En el caso de que el video se encuentre borrado o puesto en privado, se realizara una busqueda por la plataforma de Youtube. Si se logra ubicar el video en otro canal tendra un estado *copia*.