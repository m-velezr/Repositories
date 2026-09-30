package uniandes.dpoo.estructuras.logica;

import java.util.Arrays;
import java.util.HashMap;


/**
 * Esta clase tiene un conjunto de métodos para practicar operaciones sobre arreglos de enteros y de cadenas.
 *
 * Todos los métodos deben operar sobre los atributos arregloEnteros y arregloCadenas.
 * 
 * No pueden agregarse nuevos atributos.
 * 
 * Implemente los métodos usando operaciones sobre arreglos (ie., no haga cosas como construir listas para evitar la manipulación de arreglos).
 */
public class SandboxArreglos
{
    /**
     * Un arreglo de enteros para realizar varias de las siguientes operaciones.
     * 
     * Ninguna posición del arreglo puede estar vacía en ningún momento.
     */
    private int[] arregloEnteros;

    /**
     * Un arreglo de cadenas para realizar varias de las siguientes operaciones
     * 
     * Ninguna posición del arreglo puede estar vacía en ningún momento.
     */
    private String[] arregloCadenas;

    /**
     * Crea una nueva instancia de la clase con los dos arreglos inicializados pero vacíos (tamaño 0)
     */
    public SandboxArreglos( )
    {
        arregloEnteros = new int[]{};
        arregloCadenas = new String[]{};
    }

    /**
     * Retorna una copia del arreglo de enteros, es decir un nuevo arreglo del mismo tamaño que contiene copias de los valores del arreglo original
     * @return Una copia del arreglo de enteros
     */
    public int[] getCopiaEnteros( ) {
    	int[] cop = Arrays.copyOf(arregloEnteros,arregloEnteros.length);
    
        return cop;
    }


    /**
     * Retorna una copia del arreglo de cadenas, es decir un nuevo arreglo del mismo tamaño que contiene copias de los valores del arreglo original
     * @return Una copia del arreglo de cadenas
     */
    public String[] getCopiaCadenas( )
    
    {
       String[] cop = Arrays.copyOf(arregloCadenas, arregloCadenas.length);
    	
    	
    	return cop;
    }

    /**
     * Retorna la cantidad de valores en el arreglo de enteros
     * @return
     */
    public int getCantidadEnteros( )
 
    {
        
    	
    	return arregloEnteros.length;
    }

    /**
     * Retorna la cantidad de valores en el arreglo de cadenas
     * @return
     */
    public int getCantidadCadenas( )
    {
        return arregloCadenas.length;
    }

    /**
     * Agrega un nuevo valor al final del arreglo. Es decir que este método siempre debería aumentar en 1 la capacidad del arreglo.
     * 
     * @param entero El valor que se va a agregar.
     */
    public void agregarEntero( int entero )
    {
    	
    	int[] cad = new int[arregloEnteros.length + 1];

    	
    	System.arraycopy(arregloEnteros, 0, cad,0 , arregloEnteros.length );
    	
    	cad[cad.length-1] = entero;
    	arregloEnteros = cad;
    	
    	
    	
    	
    }

    /**
     * Agrega un nuevo valor al final del arreglo. Es decir que este método siempre debería aumentar en 1 la capacidad del arreglo.
     * 
     * @param cadena La cadena que se va a agregar.
     */
    public void agregarCadena( String cadena )
    {
    	String[] cad = new String[arregloCadenas.length+1];
    	System.arraycopy(arregloCadenas, 0, cad, 0,  arregloCadenas.length);
    	cad[cad.length-1]=cadena;
    	arregloCadenas = cad;
    	
    }

    /**
     * Elimina todas las apariciones de un determinado valor dentro del arreglo de enteros
     * @param valor El valor que se va eliminar
     */
    public void eliminarEntero( int valor )
    {
    	int cont=0;
    	
    	for(int i = 0; i < arregloEnteros.length; i++ ) {
    		if(arregloEnteros[i]!= valor) {
    			cont++;
    			
    		}
    		
    	}
    	
    	int[] nueva = new int[cont];
    	cont = 0;
    	for(int i = 0; i<arregloEnteros.length; i++) {
    		if(arregloEnteros[i]!= valor) {
    			nueva[cont] = arregloEnteros[i];
    			cont++;
    		}
    	}
    	arregloEnteros = nueva;
    }

    /**
     * Elimina todas las apariciones de un determinado valor dentro del arreglo de cadenas
     * @param cadena La cadena que se va eliminar
     */
    public void eliminarCadena( String cadena )
    {
    	int cont=0;
    	
    	for(int i = 0; i < arregloCadenas.length; i++ ) {
    		if(arregloCadenas[i]!= cadena) {
    			cont++;
    			
    		}
    		
    	}
    	
    	String[] nueva = new String[cont];
    	cont = 0;
    	for(int i = 0; i<arregloCadenas.length; i++) {
    		if(arregloCadenas[i]!= cadena) {
    			nueva[cont] = arregloCadenas[i];
    			cont++;
    		}
    	}
    	
    	arregloCadenas = nueva;

    }
    

    /**
     * Inserta un nuevo entero en el arreglo de enteros.
     * 
     * @param entero El nuevo valor que debe agregarse
     * @param posicion La posición donde debe quedar el nuevo valor en el arreglo aumentado. Si la posición es menor a 0, se inserta el valor en la primera posición. Si la
     *        posición es mayor que el tamaño del arreglo, se inserta el valor en la última posición.
     */
    public void insertarEntero( int entero, int posicion )
    {
    	int[] nueva = new int[arregloEnteros.length+1];
    	
    	
    	if (posicion >= arregloEnteros.length) {
    		nueva = Arrays.copyOf(arregloEnteros, arregloEnteros.length+1);
    		nueva[nueva.length-1]=entero;
    		arregloEnteros = nueva;
    	}
    	else if(posicion<0) {
    		nueva[0]=entero;
    		System.arraycopy(arregloEnteros,0,nueva,1,arregloEnteros.length);
    		arregloEnteros = nueva;
    	}
    	else {
    		int valor;
    		int cont=0;
    		for(int i =0; i<arregloEnteros.length;i++) {
    			if(i==posicion) {
    				valor = arregloEnteros[i];
    				nueva[i] = entero;
    				nueva[cont+1]= valor;
    				cont = cont+2;
    				
    			}
    			else{
    				nueva[cont]=arregloEnteros[i];
    				cont++;
    			}
    		}
    		arregloEnteros = nueva;
    	}
    	
    }

    /**
     * Elimina un valor del arreglo de enteros dada su posición.
     * @param posicion La posición donde está el elemento que debe ser eliminado. Si el parámetro posicion no corresponde a ninguna posición del arreglo de enteros, el método
     *        no debe hacer nada.
     */
    public void eliminarEnteroPorPosicion( int posicion )
    {
    	if(posicion <= arregloEnteros.length-1 && posicion >=0) {
    		int[] nueva = new int[arregloEnteros.length-1];
    		int cont =0;
    		for(int i=0;i<arregloEnteros.length;i++) {
    			if(i != posicion) {
    				nueva[cont] = arregloEnteros[i];
    				cont++;
    			}
    		}
    		arregloEnteros = nueva;
    		
    		
    		
    		
    	}

    }

    /**
     * Reinicia el arreglo de enteros con los valores contenidos en el arreglo del parámetro 'valores' truncados.
     * 
     * Es decir que si el valor fuera 3.67, en el nuevo arreglo de enteros debería quedar el entero 3.
     * @param valores Un arreglo de valores decimales.
     */
    public void reiniciarArregloEnteros( double[] valores )
    {
    	int[] nueva = new int[valores.length];
    	
    	for(int i = 0; i < valores.length;i++) {
    		nueva[i]= (int) valores[i];
    		
    	
    		
    	}
    	arregloEnteros = nueva;	
    	

    }

    /**
     * Reinicia el arreglo de cadenas con las representaciones como Strings de los objetos contenidos en el arreglo del parámetro 'objetos'.
     * 
     * Use el método toString para convertir los objetos a cadenas.
     * @param valores Un arreglo de objetos
     */
    public void reiniciarArregloCadenas( Object[] objetos )
   
    { 		
    	String[] cad = new String[objetos.length];

        
        for (int i = 0; i < objetos.length; i++) {
            cad[i] = objetos[i].toString(); 
        }

        
       arregloCadenas = cad;
    		
    }
    	
    	
    	

    

    /**
     * Modifica el arreglo de enteros para que todos los valores sean positivos.
     * 
     * Es decir que si en una posición había un valor negativo, después de ejecutar el método debe quedar el mismo valor muliplicado por -1.
     */
    public void volverPositivos( )
    {
    	for(int i =0;i<arregloEnteros.length;i++) {
    		if(arregloEnteros[i]<0) {
    			arregloEnteros[i]*=-1;
    			
    		}
    	}
    }

    /**
     * Modifica el arreglo de enteros para que todos los valores queden organizados de menor a mayor.
     */
    public void organizarEnteros( )
    {
    	Arrays.sort(arregloEnteros);
    }

    /**
     * Modifica el arreglo de cadenas para que todos los valores queden organizados lexicográficamente.
     */
    public void organizarCadenas( )
    {
    	Arrays.sort(arregloCadenas);

    }

    /**
     * Cuenta cuántas veces aparece el valor recibido por parámetro en el arreglo de enteros
     * @param valor El valor buscado
     * @return La cantidad de veces que aparece el valor
     */
    public int contarApariciones( int valor )
    {
    	int cont = 0;
        for(int val :arregloEnteros) {
        	if(val == valor) {
        		cont++;
        		
        	}
        	
        }
    	
    	
    	return cont;
    }

    /**
     * Cuenta cuántas veces aparece la cadena recibida por parámetro en el arreglo de cadenas.
     * 
     * La búsqueda no debe diferenciar entre mayúsculas y minúsculas.
     * @param cadena La cadena buscada
     * @return La cantidad de veces que aparece la cadena
     */
    public int contarApariciones( String cadena )
    {
    	int cont = 0;
    	for(String cad : arregloCadenas) {
    		if(cad.equalsIgnoreCase(cadena)) {
    			cont++;
    		}
    	}
        return cont;
    }

    /**
     * Busca en qué posiciones del arreglo de enteros se encuentra el valor que se recibe en el parámetro
     * @param valor El valor que se debe buscar
     * @return Un arreglo con los números de las posiciones del arreglo de enteros en las que se encuentra el valor buscado. Si el valor no se encuentra, el arreglo retornado
     *         es de tamaño 0.
     */
    public int[] buscarEntero( int valor )
    
    {
    	
    	int cont =0;
    
    	for(int i = 0; i<arregloEnteros.length;i++) {
    		if(arregloEnteros[i]==valor) {
    			cont++;
    			
    			
    		}	
    		
    	}
    	
    	int[] pos = new int[cont];
    	int p = 0;
    	for(int i =0; i<arregloEnteros.length;i++) {
    		if(arregloEnteros[i]== valor) {
    			pos[p]=i;
    			p++;
    		}
    	}
    	
    	return pos;
    }

    /**
     * Calcula cuál es el rango de los enteros (el valor mínimo y el máximo).
     * @return Un arreglo con dos posiciones: en la primera posición, debe estar el valor mínimo en el arreglo de enteros; en la segunda posición, debe estar el valor máximo
     *         en el arreglo de enteros. Si el arreglo está vacío, debe retornar un arreglo vacío.
     */
    public int[] calcularRangoEnteros( )
    
    {
 
    	
    	if(arregloEnteros.length == 0) {
    		return new int[0];
    		
    	}
    	else {
    		int min = Arrays.stream(arregloEnteros).min().getAsInt();
    		int max = Arrays.stream(arregloEnteros).max().getAsInt();
    	
        	return new int[]{min, max};
    	}
    }

    /**
     * Calcula un histograma de los valores del arreglo de enteros y lo devuelve como un mapa donde las llaves son los valores del arreglo y los valores son la cantidad de
     * veces que aparece cada uno en el arreglo de enteros.
     * @return Un mapa con el histograma de valores.
     */
    public HashMap<Integer, Integer> calcularHistograma( )
    {
        int val = 0;
        HashMap<Integer, Integer> mapa = new HashMap<Integer, Integer>();
    	for(int i = 0;i<arregloEnteros.length;i++) {
    		val= arregloEnteros[i];
    		int cant = 0;
    		for(int j = 0; j <arregloEnteros.length;j++ ) {
    			if(val==arregloEnteros[j]) {
    				cant++;
    				
    			}
    			
    		}
    		if (!mapa.containsKey(val)) {
    			mapa.put(val, cant);
    		}
    	}
    
    	return mapa;
    }

    /**
     * Cuenta cuántos valores dentro del arreglo de enteros están repetidos.
     * @return La cantidad de enteos diferentes que aparecen más de una vez
     */
    public int contarEnterosRepetidos( )
    {
    	HashMap<Integer, Integer> histo = calcularHistograma();
    	int tot = 0;
    	
    	for(int val: histo.values()) {
    		
    		if(val>=2) {
    			tot++;
    		}
    		
    	
    		
    		}
    	
    	
    	return tot;
    	
    }

    /**
     * Compara el arreglo de enteros con otro arreglo de enteros y verifica si son iguales, es decir que contienen los mismos elementos exactamente en el mismo orden.
     * @param otroArreglo El arreglo de enteros con el que se debe comparar
     * @return True si los arreglos son idénticos y false de lo contrario
     */
    public boolean compararArregloEnteros( int[] otroArreglo )
    
    {
    	boolean rta = false;
    	if(otroArreglo.length == arregloEnteros.length) {
    		
    		rta = true;
	        for(int i = 0; i<arregloEnteros.length;i++) {
	
	        	if(arregloEnteros[i]!=otroArreglo[i]) {
	        		rta = false;
	        		break;
	        	}
	        	
	        }
	    	
    	}
    	return rta;
    }

    /**
     * Compara el arreglo de enteros con otro arreglo de enteros y verifica que tengan los mismos elementos, aunque podría ser en otro orden.
     * @param otroArreglo El arreglo de enteros con el que se debe comparar
     * @return True si los elementos en los dos arreglos son los mismos
     */
    public boolean mismosEnteros( int[] otroArreglo )
    {
        
    	HashMap<Integer,Integer> arrA= calcularHistograma();
    	
    	if(otroArreglo.length ==0 && arregloEnteros.length ==0) {
    		return true;
    	}
    	else {
	    	boolean rta = false;
	    	int val = 0;
	        HashMap<Integer, Integer> mapa = new HashMap<Integer, Integer>();
	    	for(int i = 0;i<otroArreglo.length;i++) {
	    		val= otroArreglo[i];
	    		int cant = 0;
	    		for(int j = 0; j <otroArreglo.length;j++ ) {
	    			if(val==otroArreglo[j]) {
	    				cant++;
	        			
	    				
	    			}
	    			
	    		}
	    		if (!mapa.containsKey(val)) {
	    			mapa.put(val, cant);
	    		}
	    	}
	    	
	    	for(int v:arregloEnteros) {
	    		if(arrA.get(v)==mapa.get(v)) {
	    			rta = true;
	    		}
	    	}
	    	
	    	
	    	
	    	
	    	
	    	return rta;
    	}
    }

    /**
     * Cambia los elementos del arreglo de enteros por una nueva serie de valores generada de forma aleatoria.
     * 
     * Para generar los valores se debe partir de una distribución uniforme usando Math.random().
     * 
     * Los números en el arreglo deben quedar entre el valor mínimo y el máximo.
     * @param cantidad La cantidad de elementos que debe haber en el arreglo
     * @param minimo El valor mínimo para los números generados
     * @param maximo El valor máximo para los números generados
     */
    public void generarEnteros( int cantidad, int minimo, int maximo )
    {
     
    	int[] nueva = new int[cantidad];
    	
    	
    	for(int i = 0; i< cantidad;i++) {
    		nueva[i]= minimo + (int)(Math.random() * (maximo - minimo + 1));
    		

    	}
    	
    	arregloEnteros = nueva;
    			
    }

}
