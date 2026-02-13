// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>

// Enumeración para días de la semana
// Las enumeraciones permiten definir conjuntos de constantes enteras asociadas con nombres.
// En este caso, los días de la semana se asignan de 0 a 6 automáticamente.
enum DiaSemana {
    LUNES,     // 0
    MARTES,    // 1
    MIERCOLES, // 2
    JUEVES,    // 3
    VIERNES,   // 4
    SABADO,    // 5
    DOMINGO    // 6
};

// Enumeración para direcciones cardinales
// Similarmente, las direcciones cardinales se representan por constantes enteras.
enum Direcciones {
    NORTE,     // 0
    SUR,       // 1
    ESTE,      // 2
    OESTE      // 3
};

// Enumeración para notas musicales
// También usamos una enumeración para representar las notas musicales.
// Agregamos NUM_NOTAS como una forma de contar cuántas notas hay, sin asignarle un valor explícito.
enum NotasMusicales {
    DO,        // 0
    RE,        // 1
    MI,        // 2
    FA,        // 3
    SOL,       // 4
    LA,        // 5
    SI,        // 6
    NUM_NOTAS  // 7 (sirve para saber cuántas notas hay)
};

// Estructura que representa una fecha, incluyendo el día de la semana (usando enum)
// Las estructuras permiten agrupar diferentes tipos de datos bajo un solo nombre.
struct fecha {
    unsigned int dia;         // Día del mes
    unsigned int mes;         // Mes del año
    unsigned int año;         // Año
    enum DiaSemana dia_semana; // Día de la semana usando la enumeración
};

// Array constante de frecuencias para cada nota
// El array "frecuencias" almacena las frecuencias correspondientes a cada nota musical.
// El índice coincide con el valor de la enumeración NotasMusicales.
const double frecuencias[NUM_NOTAS] = {
    261.63, // DO
    293.66, // RE
    329.63, // MI
    349.23, // FA
    392.00, // SOL
    440.00, // LA
    493.88  // SI
};

int main(void) {
    // Ejemplo 1: Uso de enum para días de la semana
    // Asignamos el valor MARTES (1) a la variable hoy de tipo enum DiaSemana
    enum DiaSemana hoy = MARTES;
    printf("Hoy es %d\n", hoy); // Imprimimos el valor entero de MARTES (1)

    // Ejemplo 2: Uso de enum para direcciones cardinales
    // Asignamos la dirección NORTE (0) a la variable direccion de tipo enum Direcciones
    enum Direcciones direccion = NORTE;
    printf("La dirección es %d\n", direccion); // Imprimimos el valor entero de NORTE (0)

    // Ejemplo 3: Asignación de valores específicos a enum
    // Definimos otra enumeración para los meses del año. Los valores son explícitos,
    // comenzando por ENERO = 1, y los siguientes valores son asignados automáticamente.
    enum Meses {
        ENERO = 1,
        FEBRERO,
        MARZO,
        ABRIL,
        MAYO,
        JUNIO,
        JULIO,
        AGOSTO,
        SEPTIEMBRE,
        OCTUBRE,
        NOVIEMBRE,
        DICIEMBRE
    };
    enum Meses mes_actual = ABRIL; // Asignamos el valor ABRIL (4)
    printf("Estamos en el mes %d\n", mes_actual); // Imprimimos el valor de ABRIL (4)

    // Ejemplo 4: Uso de enumeración y acceso al array de frecuencias
    // Asignamos la nota MI (2) y usamos ese valor como índice en el array frecuencias
    enum NotasMusicales nota_actual = MI;
    printf("La frecuencia de la nota MI es %.2f Hz\n", frecuencias[nota_actual]);

    // Ejemplo 5: Uso de una estructura para almacenar una fecha
    // Creamos una variable de tipo struct fecha y asignamos valores a sus miembros
    struct fecha f;
    f.dia = 13;
    f.mes = 12;
    f.año = 2005;
    f.dia_semana = VIERNES; // Asignamos el día de la semana usando la enumeración
    printf("fecha -> %d/%d/%d ", f.dia, f.mes, f.año); // Imprimimos la fecha sin el día de la semana

    // Usamos un switch para imprimir el día de la semana de forma textual
    switch (f.dia_semana) {
        case LUNES:
            printf("LUNES");
            break;
        case MARTES:
            printf("MARTES");
            break;
        case MIERCOLES:
            printf("MIERCOLES");
            break;
        case JUEVES:
            printf("JUEVES");
            break;
        case VIERNES:
            printf("VIERNES");
            break;
        default:
            break;
    }
    printf("\n");

    return 0;
}
