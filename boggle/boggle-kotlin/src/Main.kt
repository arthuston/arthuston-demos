/**
 * Run boggle using file argument as input.
 */
package com.arthuston.demos.boggle;


import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

public class Main {

    public static void main(String[] args) throws IOException {
        if (args.length != 1) {
            System.err.println("Usage: Main <input-file>");
            System.exit(1);
        }

        String[] puzzle = null;
        Set<String> words = null;

        try (InputStream is = new FileInputStream(args[0])) {
            Scanner scanner = new Scanner(is);
            puzzle = readPuzzle(scanner);
            words = readWords(scanner);
        }

        // solve puzzle
        Boggle boggle = new Boggle(puzzle);
        List<String> foundWords = boggle.solve(words);

        // print result
        System.out.println("Found:");
        for (String foundWord : foundWords) {
            System.out.println(foundWord);
        }

        System.exit(0);
    }

    /**
     * Read puzzle from stdin.
     *
     * @param scanner input scanner
     * @return puzzle
     */
    private static String[] readPuzzle(Scanner scanner) {
        int puzzleSize = scanner.nextInt();
        String[] puzzle = new String[puzzleSize];
        System.out.println("Puzzle:");
        for (int i = 0; i < puzzleSize; i++) {
            puzzle[i] = scanner.next();
            System.out.println(puzzle[i]);
            if (puzzle[i].length() != puzzleSize) {
                throw new IllegalArgumentException(String.format("%s is the wrong length, expected %d",
                        puzzle[i], puzzleSize));
            }
        }
        System.out.println();
        return puzzle;
    }

    private static Set<String> readWords(Scanner in) {
        /**
         * Read set of words from stdin.
         * @param in input scanner
         * @return set of words
         */
        int wordSize = in.nextInt();
        Set<String> words = new HashSet<>();
        System.out.println("Words:");
        for (int i = 0; i < wordSize; i++) {
            String word = in.next();
            words.add(word);
            System.out.println(word);
        }
        System.out.println();
        return words;
    }
}