# Compras del homelab — fase 1

Consulta de precios: noche del lunes 23 de noviembre de 2026 (Ciudad de México).
Presupuesto tope: **$4,500 MXN**.
Los precios de abajo son una foto de esa noche. Hay que reabrir el enlace antes de pagar.

## Equipo que ya está en casa

| Pieza | Rol |
| --- | --- |
| PC de escritorio | Servidor. Destino: Proxmox VE, o Debian con Docker. |
| SSD NVMe 500 GB | Sistema y contenedores. |
| 2 discos HDD | Almacenamiento en espejo (RAID 1). |
| PC Windows de uso diario | Máquina de administración: consola serie, SSH, Rufus para el instalador. |
| MacBook M1 Max | Respaldo de administración. El cable USB-A le queda con un adaptador USB-C. |

La torre del servidor se queda en el piso. El rack de esta fase carga el switch, un patch panel y una PDU. Un gabinete de pared de 12U no admite una torre.

## Qué cambia con la PC Windows

La PC Windows baja el costo del cable de consola y deja la configuración en PuTTY. Windows Update instala el driver del chip FTDI. El puerto USB-A de esa PC evita el cable USB-C que pedía la Mac.

Eso ahorra del orden de **$100 a $200 MXN**. El mercado del switch no se mueve: un Catalyst Gigabit con número de parte verificable sigue arriba de **$6,000 MXN** usado. Con $4,500 no salen rack, cable y un 2960-X confirmado el mismo día.

## Compra de hoy

| Pieza | Qué comprar | Precio visto |
| --- | --- | --- |
| Rack | StarTech RK12OD. Abierto, 2 postes, 19 pulgadas, 12U, piso o escritorio, EIA-310, 50 kg, incluye cage nuts. | $1,229 + envío $300 en Cyberpuerta |
| Cable | OIKWAN USB-A a RJ45, chip FTDI FT232RL, 1.8 m. Entra al puerto USB-A de la PC Windows y al RJ45 azul marcado CONSOLE del switch. | $319.99 + envío $78.67 (vendedor del extranjero). Respaldo con más reseñas: el azul a $533.69, importación incluida. |
| Switch | Ninguno hoy. | Se reservan unos $2,570 |

Total comprometido hoy: **$1,628** con el cable de $320, o **$2,063** con el azul de $534. En ambos casos el envío del rack ya va dentro. Quedan entre **$2,400 y $2,870** para el switch. Con eso se puede tomar un Gigabit usado si el anuncio pasa la auditoría de más abajo. Un 2960-X de tienda reacondicionada sigue fuera de alcance.

El mismo cable FTDI funciona en la MacBook con un adaptador USB-C a USB-A. El puerto mini-USB de consola que traen algunos 2960-X usa el driver de Cisco, que en Apple Silicon no es nativo. El RJ45 de consola es el puerto correcto en las dos máquinas.

## Tabla comparativa

| Producto | Tienda | Precio MXN | Link | Pros / contras |
| --- | --- | --- | --- | --- |
| StarTech RK12OD, rack abierto 12U 2 postes 19" | Cyberpuerta | $1,229 + envío $300. 16 piezas. | [Categoría StarTech](https://www.cyberpuerta.mx/Racks-y-Gabinetes-Startech-com/) · [ficha RK12OD](https://www.startech.com/en-us/server-management/rk12od) | Pros: 12U, EIA-310, 50 kg, cage nuts, garantía de por vida, deja presupuesto para el switch. Contras: es de piso o escritorio, profundidad de base ~29 cm. Un 24TS-L cabe; un PoE profundo sobresale por atrás, aceptable en marco abierto. |
| Intellinet 716192, rack abierto de pared 12U 2 postes | PC Digital | $2,914. 11 piezas. | [PC Digital](https://www.pcdigital.com.mx/rack-abierto-19-intellinet-12u-para-montaje-en-pared-hasta-30-kg-color-negro-716192/) | Pros: el modelo pedido, pared, 400 mm útiles, tornillería incluida. Contras: se come el presupuesto del switch. Carga 30 kg (10 kg con el marco abierto). |
| Intellinet 716192 | Zegucom | Desde $2,610.84 | [Zegucom](https://www.zegucom.com.mx/producto/redes/panel-de-parcheo/panel-intellinet-716192-material-acero-peso-max-30-kg-tornillos-inclu/NzE2MTky) | Mismo rack, otro vendedor. Confirmar existencia el día de la compra. |
| Intellinet rack abierto de pared 12U, hasta 40 kg | Cyberpuerta | $2,899 + envío $563. 3 piezas. | [Cyberpuerta](https://www.cyberpuerta.mx/Computo-Hardware/Servidores/Accesorios-para-Servidores/Racks-y-Gabinetes/Intellinet-Rack-Abierto-para-Pared-19-12U-hasta-40-kg-Negro.html) | Puede ser un hermano del 716192. Hay que leer el número de parte en la ficha antes de pagarlo. |
| Intellinet 715966, rack de piso 22U 2 postes, 200 kg | Cyberpuerta | $1,879 + envío $773. 9 piezas. | [Cyberpuerta](https://www.cyberpuerta.mx/Computo-Hardware/Servidores/Accesorios-para-Servidores/Racks-y-Gabinetes/Intellinet-Rack-Abierto-19-715966-22U-hasta-200kg.html) | Pros: más unidades y más carga, mejor a futuro. Contras: aterriza cerca de $2,650 y deja ~$1,500 para el switch. |
| Enson ENS-RACKW12U, rack de pared 12U | Cyberpuerta | $959 + envío $270. 10 piezas. | [Cyberpuerta](https://www.cyberpuerta.mx/Computo-Hardware/Servidores/Accesorios-para-Servidores/Racks-y-Gabinetes/Enson-Rack-de-Pared-12U-Negro.html) | Precio bajo. La ficha no confirma rieles EIA-310 ni carga. Fuera de la compra hasta ver especificaciones. |
| OIKWAN USB-A a RJ45, FTDI FT232RL, negro, 1.8 m | Amazon México | $319.99 + envío $78.67 | [B0DPZZJBZ2](https://www.amazon.com.mx/Essential-Accesory-Compatible-Ubiquity-Switches/dp/B0DPZZJBZ2) | Pros: chip FTDI, USB-A para la PC Windows, pinout de consola Cisco. Contras: vendedor del extranjero; revisar plazo de entrega. |
| OIKWAN USB-A a RJ45, FTDI FT232RL, azul, 1.8 m | Amazon México | $533.69, importación incluida | [B075V1RGQK](https://www.amazon.com.mx/OIKWAN-Console-Routers-Router-Windows/dp/B075V1RGQK) | Miles de reseñas (4.6). Es el respaldo si el negro tarda o cambia de chip. |
| JESWO USB-A a RJ45, FT232R, 1.8 m | Amazon México | Listado en $249 y agotado esa noche | [B0CLLBDLHR](https://www.amazon.com.mx/JESWO-Conductor-Consola-Routers-Switches/dp/B0CLLBDLHR) | El chip correcto y más barato. Sin existencia el 23 de noviembre de 2026. |
| IQlionco USB-C a RJ45, anuncio FT232RL, 3 m | Amazon México | $340.55 | [B0FZJQDSZR](https://www.amazon.com.mx/dp/B0FZJQDSZR) | Sirve en la Mac sin adaptador y en una PC con USB-C. Pocas reseñas. Comprarlo solo si la ficha sigue diciendo FT232RL. |
| Cable consola USB a RJ45, Mercado Libre, +100 vendidos | Mercado Libre | $186 a $236 | [Listado](https://listado.mercadolibre.com.mx/venta-de-switch-router-cisco) | Precio bajo y envío local. El anuncio no nombra el chip. Muchos de este rango son Prolific clonado. |
| DSD TECH SH-RJ45P, chip Prolific PL2303GT | Amazon México | $254.99 | [B0F62Z5YK8](https://www.amazon.com.mx/dp/B0F62Z5YK8) | En Windows 11 el PL2303GT suele funcionar. El PL2303HXA viejo da error de driver. Queda fuera: la regla es FTDI. |
| WS-C2960X-24TS-L nuevo, 24× Gigabit + 4 SFP | Digitalife | $45,106.10 | [Digitalife](https://www.digitalife.com.mx/productos/switch-cisco-24-puertos-catalyst-2960x-101001000mbps-gigabite-rack-administrable-4x-sfp) | El modelo ideal, nuevo, fuera de presupuesto. |
| WS-C2960X-24PS-L reacondicionado, Gigabit PoE | Mercado Libre | $6,000 a $7,500 los avisos bajos; hay piezas de $9,800 a $21,999 | [Listado 2960](https://listado.mercadolibre.com.mx/switch-cisco-catalyst-2960-24tt-l) | Gigabit real. PoE, ventiladores y consumo altos para un departamento. Arriba del tope en cuanto se suma el rack. |
| WS-C2960S-24TS-L, 24× Gigabit + 4 SFP | Mercado Libre, internacional | $9,994 | Mismo listado | Gigabit correcto. Precio de importación, arriba del tope. |
| WS-C2960S-24TD-L anunciado en $980 | Mercado Libre | $980, envío gratis | Dentro del [listado 2960](https://listado.mercadolibre.com.mx/switch-cisco-catalyst-2960-24tt-l). La ficha pide sesión. | Si la etiqueta es real: 24× Gigabit y 2× SFP+ 10G, la mejor pieza del presupuesto. A ese precio hay que ver foto de la etiqueta antes de pagar. |
| “Switch Cisco 2960-x 24 Ptos” | Mercado Libre | $1,900 | Mismo listado | El título no trae número de parte. Puede ser un 2960 Fast Ethernet con una X en el nombre. |
| WS-C2960X-48FPS-L usado | Mercado Libre | $4,500 | [Publicación](https://www.mercadolibre.com.mx/switch-cisco-wsc2960x48fpsl-gigabit-poe/up/MLMU3207606993) | 48 puertos Gigabit PoE+. Se lleva el presupuesto entero, es ruidoso y el vendedor escribió “1 GB/s” de capacidad. El equipo real anda cerca de 216 Gbps. |
| WS-C2960-24TT-L usado | Mercado Libre | $720 a $2,800 | Mismo listado | 24 puertos 10/100 y dos uplinks Gigabit. Descartado. |

## Modelos de switch que sí entran

En este orden, todos con los 24 puertos de cobre en 10/100/1000:

1. `WS-C2960X-24TS-L` — LAN Base, sin PoE, el que conviene en un departamento.
2. `WS-C2960S-24TS-L` o `WS-C2960S-24TD-L` — el 24TD-L suma 2 puertos SFP+ de 10G.
3. `WS-C3560X-24T-S` — capa 3, útil para practicar ruteo. Suele salir más caro.

`WS-C2960X-24PS-L` y el resto PoE (`PS`, `PD`, `FPS`) solo si más adelante hace falta alimentar access points. La fuente y los ventiladores suben ruido y el recibo de luz.

## Modelos que se descartan aunque el anuncio diga “Cisco 24 puertos”

- `WS-C2960-24TT-L`, `48TT-L`: Fast Ethernet, con dos uplinks Gigabit.
- `WS-C2960-24TC-L`, `24PC-L`, `24PC-S`: cobre a 10/100.
- Cualquier anuncio que diga 10/100, “Ethernet” a secas, o que no muestre el número de parte en la etiqueta.

## Auditoría de un anuncio usado

Pasar el enlace por aquí antes de pagar. Hace falta todo esto:

1. Foto de la etiqueta trasera con el PID (`WS-C2960X-24TS-L` o uno de la lista de arriba) y el número de serie.
2. Foto del frente donde los puertos de cobre se lean 10/100/1000.
3. Respuesta del vendedor: orejas de rack incluidas, enciende, ventiladores giran, sin olor a quemado.
4. Si tiene contraseña. En IOS se puede borrar por el modo de recuperación, salvo que alguien haya puesto `no service password-recovery`.
5. Video corto de un puerto negociando 1 Gbps con una laptop.
6. Publicación nacional, con devolución. Las que dicen “para partes”, “no enciende” o “internacional” se dejan pasar.

Sin la foto de la etiqueta, el anuncio de $980 y el de $1,900 se quedan en espera.

## Auditoría 2026-11-23 — gabinete de Mercado Libre

Publicación vista en captura a las 23:30 (Ciudad de México). Enlace corto del chat: [meli.la/1nnCXqW](https://meli.la/1nnCXqW), artículo `MLM6459824462`.

| Dato | Lo que muestra la publicación |
| --- | --- |
| Título | Gabinete de pared 19" 12U, rack o bastidor |
| Medida en la foto | 600 × 600 × 600 mm, “Gabinete de redes 12U” |
| Precio | $2,007.46 (tachado $4,599, 56% menos). IVA incluido |
| Envío | Gratis, llega al día siguiente. +25 vendidos. Más vendido, 7° en gabinetes para servidores |
| Foto | Gabinete cerrado, puerta de cristal, parece llevar ruedas. Foto 2 de 12, estilo catálogo |

Veredicto: **sí, en lugar del StarTech RK12OD, solo si el vendedor confirma cuatro cosas.** El fondo de 600 mm le queda bien a un Catalyst (el chasis anda entre 280 y 370 mm). El RK12OD tiene unos 290 mm de base y el equipo sobresale. La torre del servidor no entra en 12U; se queda en el piso igual que con el rack abierto.

Preguntas antes de pagar:

1. El título dice “de pared” y la foto es de piso con ruedas. Cuál de los dos se envía.
2. Rieles EIA de 19 pulgadas, tuercas enjauladas y tornillos incluidos.
3. Las ruedas de la foto vienen en la caja.
4. Costados perforados. Un 2960 sin PoE vive bien ahí. Un modelo PoE, dentro de una puerta de cristal, calienta y se oye más.

Si esas cuatro salen bien, el gasto queda así: gabinete $2,007, cable FTDI unos $400, y cerca de **$2,090** para el switch. El precio de $4,599 tachado es el “antes” habitual de Mercado Libre; $2,007 es un precio normal de gabinete genérico, no una ganga. Sin respuesta sobre los rieles, no se paga.
