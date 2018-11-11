package com.test.testfilter;

import java.util.AbstractList;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Random;

public class TestFilter {

	static int[] sizes = {100, 250, 500, 1000, 2500,5000, 10000, 25000,50000,100000};
	static int[] repeats = {100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100};
	
	static Random random;
			
	public static void main(String[] args) {
		random = new Random(System.currentTimeMillis());
		for(int index = 0; index < sizes.length; index++) {
			int size = sizes[index];
			int repeat = repeats[index];
			System.out.println("Use array size " + size + " (repeated " + repeat + " times)" );
			test1(size, repeat);
			test2(size, repeat);
			test3(size, repeat);
			System.out.println("----------------------------------------");
		}
	}

	static public void test1(int size, int repeat) {
		long startTime = System.nanoTime(); 	
		for(int r = 0; r < repeat; r++) {
			AbstractList<Integer> l = createRandomArray(size, 0);
			AbstractList<Integer> l1 = filterEvenRemove(l);
			
		}
		long estimatedTime = System.nanoTime() - startTime;
		System.out.println("Filter ArrayList with remove   :" + estimatedTime);			
	}
	
	static public void test2(int size, int repeat) {
		long startTime = System.nanoTime(); 	
		for(int r = 0; r < repeat; r++) {
			AbstractList<Integer> l = createRandomArray(size, 1);
			AbstractList<Integer> l1 = filterEvenRemove(l);
			
		}
		long estimatedTime = System.nanoTime() - startTime;
		System.out.println("Filter LinkedList with remove  :" + estimatedTime);			
		
	}

	static public void test3(int size, int repeat) {
		long startTime = System.nanoTime(); 	
		for(int r = 0; r < repeat; r++) {
			AbstractList<Integer> l = createRandomArray(size, 1);
			AbstractList<Integer> l1 = filterEvenAdd(l);
		}
		long estimatedTime = System.nanoTime() - startTime;
		System.out.println("Filter ArrayList with new list :" + estimatedTime);			
		
	}
	
	static AbstractList<Integer> filterEvenRemove(AbstractList<Integer> in) {
		Iterator<Integer> it = in.iterator();
		while(it.hasNext()) {
			Integer i = it.next();
			if( (i.intValue() & 1) == 1) {
				it.remove();
			}
		}
		return in;
	}
	
	static AbstractList<Integer> filterEvenAdd(AbstractList<Integer> in) {
		AbstractList<Integer> result = new ArrayList(in.size());
		Iterator<Integer> it = in.iterator();
		while(it.hasNext()) {
			Integer i = it.next();
			if( (i.intValue() & 1) != 1) {
				result.add(i);
			}
		}
		return result;
	}
	

	static AbstractList<Integer> createRandomArray(int size, int type) {
		AbstractList<Integer> result;
	 
		if( type == 0) {
			result = new ArrayList<Integer>(size);
		} else {
			result = new LinkedList<Integer>();
		}
		for(int i = 0; i < size; i++) {
			result.add(random.nextInt());
		}
		return result;
	}	
}
