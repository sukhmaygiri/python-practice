{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPAFpPPhlWMBY7QplxrOp9R",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sukhmaygiri/python-practice/blob/main/tuple\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JuUZwo30Wy3a",
        "outputId": "985893b9-38cd-4094-9960-563e083ec183"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(10, 'hello', 20)\n",
            "()\n"
          ]
        }
      ],
      "source": [
        "t1=(10,\"hello\",20)\n",
        "print(t1)\n",
        "t2=()\n",
        "print(t2)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t2=(1,2,3,4,5,6,7,8,9,10)\n",
        "print(\"3rd element=\",t2[2])\n",
        "print(\"4th element from end =\",t2[-4])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X6-PEosqXG_k",
        "outputId": "143485c6-5b4a-4f6d-903c-21c86f3ea1d2"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3rd element= 3\n",
            "4th element from end = 7\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t3=(1,2,3,4,5,6)\n",
        "t3=t3+(7,)\n",
        "print(t3)\n",
        "t3=tuple(list(t3)+[8])\n",
        "print(t3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cAEO58YTX_Ys",
        "outputId": "2a6ce2a2-4da0-4da7-e9cf-a4fabb40c24c"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(1, 2, 3, 4, 5, 6, 7)\n",
            "(1, 2, 3, 4, 5, 6, 7, 8)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t = (1, 2, 3, 2, 4, 2)\n",
        "print(\"Occurrences of 2:\", t.count(2))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3klWoZtbYzQH",
        "outputId": "1bf7ecda-6914-4ea0-cd43-323c2849650f"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Occurrences of 2: 3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t4=(1,2,3,64,65,46,27,38,19,10)\n",
        "for i in range(len(t4)):\n",
        "  if i%2==0:\n",
        "    print(t4[i])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JPM-MccQZII9",
        "outputId": "43af6400-3a58-4dad-f77a-09f5c1cdb9d8"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "3\n",
            "65\n",
            "27\n",
            "19\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t4=(1,2,3,64,65,46,27,38,19,10)\n",
        "new_list=[]\n",
        "for i in range(len(t4)):\n",
        "  if i%2!=0:\n",
        "    new_list.append(t4[i])\n",
        "print(new_list)\n",
        ""
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yCQiO-A9ZuCl",
        "outputId": "46f6e301-aafd-4b2b-8876-70fb8d746d0f"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[2, 64, 46, 38, 10]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t4=(1,2,3,64,65,46,27,38,19,10)\n",
        "new_list=[]\n",
        "for i in range(len(t4)):\n",
        "  if t4[i]%2==0:\n",
        "    new_list.append(t4[i])\n",
        "print(new_list)\n",
        ""
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "H7hLk0QAa08d",
        "outputId": "0c36f7e9-7e30-42b9-dea5-70d23011a6e7"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[2, 64, 46, 38, 10]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t = (1, 2, 3, 4)\n",
        "print(\"Reversed (built-in):\", tuple(reversed(t)))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XnajaybPbfct",
        "outputId": "d0312383-e664-47aa-ff6d-7e27fbccc8ca"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Reversed (built-in): (4, 3, 2, 1)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t4=(1,2,3,64,65,46,27,38,19,10)\n",
        "templist=list(t4)\n",
        "templist.sort()\n",
        "templist.reverse()\n",
        "t4=tuple(templist)\n",
        "print(t4)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Qq2kMIp1dWYC",
        "outputId": "484f95f4-9758-413e-d41d-b6653ce91737"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(65, 64, 46, 38, 27, 19, 10, 3, 2, 1)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "mix_tuple=(2,3.4,\"hello\",16)\n",
        "square=[]\n",
        "for i in mix_tuple:\n",
        "  if type(i)==int:\n",
        "    square.append(i**2)\n",
        "  if type(i)==float:\n",
        "    square.append(i**2)\n",
        "print(square)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QDTBLpOzeuVO",
        "outputId": "e4896770-8b61-4df7-c3ed-4ccf1ab2ab16"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[4, 11.559999999999999, 256]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t = (10, 20, 30, 10)\n",
        "\n",
        "print(\"Result:\", t[0] == t[-1])\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "azVOBBbNgJzN",
        "outputId": "74fdf66c-982c-48c3-b55a-bbf37583877a"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Result: True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t = (10, 12, 15, 22, 25)\n",
        "\n",
        "for x in t:\n",
        "    if x % 5 == 0:\n",
        "        print(x)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WFxJ-jtNgT9Z",
        "outputId": "6c661d6e-f998-4d04-bf2c-f9db62a622d0"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10\n",
            "15\n",
            "25\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t = (1, 2, 3, 4, 5, 6)\n",
        "\n",
        "even_t = tuple(x for x in t if x % 2 == 0)\n",
        "print(\"Even tuple:\", even_t)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RvXXqVKagVyU",
        "outputId": "1289bc12-e3fe-4878-bccf-241a87876fed"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Even tuple: (2, 4, 6)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 1. Take multiple inputs separated by spaces\n",
        "user_input = input(\"Enter numbers separated by space: \")\n",
        "\n",
        "# 2. Convert input string into a tuple of integers\n",
        "tup = tuple(int(x) for x in user_input.split())\n",
        "\n",
        "# 3. Logic to find the largest without max()\n",
        "if len(tup) > 0:\n",
        "    largest = tup[0]  # Assume the first one is the largest\n",
        "\n",
        "    for num in tup:\n",
        "        if num > largest:\n",
        "            largest = num\n",
        "\n",
        "    print(\"The largest number is:\", largest)\n",
        "else:\n",
        "    print(\"The tuple is empty.\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "o3vdPcWwgyDM",
        "outputId": "ecdeb762-ab5c-49c0-f470-12aa700663ed"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter numbers separated by space: 12 12 54 26\n",
            "The largest number is: 54\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "lst = [(1,2,3), (4,5,6), (7,8,9)]\n",
        "\n",
        "new_lst = [t[:-1] + (100,) for t in lst]\n",
        "print(new_lst)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "o0mtOnuRh_Xt",
        "outputId": "7e07deb7-6946-44db-bb85-829f1c277ced"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[(1, 2, 100), (4, 5, 100), (7, 8, 100)]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "XBLHB0xBiO1N"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
