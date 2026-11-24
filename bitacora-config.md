# Bitácora de configuración

Registro de lo que ya se hizo en los equipos. Lo que sigue es el índice de la fase 2. Los comandos se pegan aquí el día que el switch y la torre estén conectados, con la salida real de la consola.

## 2026-11-23 — Sin equipos nuevos

- Compras definidas en [compras.md](compras.md). Rack y cable recomendados. Switch en espera de un anuncio Gigabit auditado.
- Máquina de administración: PC Windows. Herramienta prevista para la consola: PuTTY, sesión Serial, 9600 baudios, 8 bits de datos, sin paridad, 1 bit de paro, sin control de flujo. El puerto sale como `COMx` cuando Windows reconoce el FTDI.
- La MacBook queda de respaldo. En esa máquina la sesión sería `screen` o `minicom` sobre `/dev/cu.usbserial-*`, a 9600, con adaptador USB-C si el cable es USB-A.

## Fase 2 — pendiente de que llegue el equipo

1. Consola serie desde la PC Windows al puerto RJ45 CONSOLE del switch.
2. Confirmación del modelo con la etiqueta y con la salida de arranque. Si el PID es Fast Ethernet, se detiene y se gestiona la devolución.
3. Reset de fábrica y configuración base de IOS: nombre, contraseña, dirección de gestión, SSH.
4. VLAN de la casa y VLAN del servidor. El detalle queda en [topologia.md](topologia.md) en la misma sesión.
5. Instalador de Proxmox VE (o Debian) en la torre, hecho con Rufus desde la PC Windows. NVMe de 500 GB para el sistema. Los dos HDD para el espejo de datos.
