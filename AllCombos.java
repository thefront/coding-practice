public class AllCombos {
  private static void combination(String prefix, String str) {
    int n = str.length();
    System.out.println(prefix);
    for (int i = 0; i < n; i++) {
      combination(prefix + str.charAt(i), str.substring(0, i) +
                    str.substring(i+1));
    }
  }

  public static void main(String[] args) {
    combination("", "abc");
  }
}
