{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "dfaf1f31",
   "metadata": {},
   "source": [
    "# Python Temel Bitirme Projesi - Rafig Novruzov
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c15bbeba",
   "metadata": {},
   "source": [
    "**1. SORU:**   \n",
    "Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listtlerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:\n",
    "\n",
    "`input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]\n",
    "output: [1,'a','cat',2,3,'dog',4,5]`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "f8586fb8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 'a', 'cat', 2, 3, 'dog', 4, 5]"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def duz(liste):\n",
    "    for oge in liste:\n",
    "        if isinstance(oge, list):\n",
    "            yield from duz(oge)\n",
    "        else:\n",
    "            yield oge\n",
    "\n",
    "\n",
    "liste = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]\n",
    "duz_liste = [a for a in duz(liste)]\n",
    "\n",
    "duz_liste"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "28c56fb2",
   "metadata": {},
   "source": [
    "**2. SORU:**\n",
    "Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:\n",
    "\n",
    "`input: [[1, 2], [3, 4], [5, 6, 7]]\n",
    "output: [[[7, 6, 5], [4, 3], [2, 1]]`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "3b18175d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[7, 6, 5], [4, 3], [2, 1]]"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "liste2 = [[1, 2], [3, 4], [5, 6, 7]]\n",
    "for i in liste2:\n",
    "    i.reverse()\n",
    "liste2.reverse()\n",
    "\n",
    "liste2"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}