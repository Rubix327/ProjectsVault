import java.util.*;

public class Main {

    public static void main(String[] args) {
        System.out.println(unknownDataTypeSum(0, 5, 10, -5, 3.14, -9) + " :: Should be 4.14");
        System.out.println(unknownDataTypeSum(true, false, false, true) + " :: Should be true");
        System.out.println(unknownDataTypeSum("lorem", " ipsum", " dolor", " sit", " ", "amet") + " :: Should be lorem ipsum dolor sit amet");
    }

    public static void testTypes(){
        printTypeOf(0);
        printTypeOf(0.1);
        printTypeOf(-5);
        printTypeOf("string");
        printTypeOf(true);
        printTypeOf(false);
        printTypeOf("false");
    }

    public static Object unknownDataTypeSum(Object... objects){
        Set<Class<?>> objectTypes = new HashSet<>();

        for (Object object : objects) {
            if (object instanceof String){
                objectTypes.add(String.class);
            } else if (object instanceof Number){
                objectTypes.add(Number.class);
            } else if (object instanceof Boolean){
                objectTypes.add(Boolean.class);
            } else {
                throw new IllegalArgumentException("Only Strings, Numbers and Booleans are acceptable.");
            }
        }

        if (objectTypes.isEmpty()){
            throw new IllegalArgumentException("Set of objects is empty.");
        }
        if (objectTypes.size() > 1){
            throw new IllegalArgumentException("Objects are not of the same class.");
        }

        List<Class<?>> objectTypesList = new ArrayList<>(objectTypes);
        Class<?> type = objectTypesList.get(0);
        if (type.equals(String.class)){
            StringBuilder concat = new StringBuilder();
            for (Object object : objects) {
                concat.append((String) object);
            }
            return concat.toString();
        }
        else if (type.equals(Number.class)){
            double d = 0d;
            for (Object object : objects) {
                if (object instanceof Integer){
                    d += (Integer) object;
                } else if (object instanceof Long){
                    d += (Long) object;
                } else if (object instanceof Double){
                    d += (Double) object;
                } else if (object instanceof Float){
                    d += (Float) object;
                }
            }
            return d;
        }
        else if (type.equals(Boolean.class)){
            boolean result = false;
            for (Object object : objects) {
                boolean boolObject = (boolean) object;
                result = result || boolObject;
            }
            return result;
        }

        return null;
    }

    public static void printTypeOf(Object object){
        System.out.println("-----------");
        System.out.println("-> " + object.toString() + " :: " + object.getClass());
        System.out.println("   " + (object instanceof Number ? "- is number" : "- is NOT number"));
        System.out.println("   " + (object instanceof String ? "- is string" : "- is NOT string"));
        System.out.println("   " + (object instanceof Boolean ? "- is boolean" : "- is NOT boolean"));
        System.out.println("-----------");
    }

}