{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Github常用代码.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMWUz1AZVB4U/yE0HnrfTrR",
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
        "<a href=\"https://colab.research.google.com/github/qiaoyanxie/learning/blob/main/Github%E5%B8%B8%E7%94%A8%E4%BB%A3%E7%A0%81.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "X2eVbV7pK_k4"
      },
      "source": [
        "# 挂在google drive\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-DJvfyeOK4rp",
        "outputId": "8d2eeeed-0ee8-408c-ea21-b53f3a1d8189"
      },
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TMqx_asKOOGX"
      },
      "source": [
        "# 下载数据集以及文件"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1B8LstIQOR3B"
      },
      "source": [
        "!echo \"Downloading train zarr dataset...\"\n",
        "!wget https://lyft-l5-datasets-public.s3-us-west-2.amazonaws.com/prediction/v1.1/train.tar \\\n",
        "    -q --show-progress -P $TEMP_DOWNLOAD_DIR\n",
        "\n",
        "!mkdir -p $TEMP_DATASET_DIR/scenes\n",
        "!tar xf $TEMP_DOWNLOAD_DIR/train.tar -C $TEMP_DATASET_DIR/scenes\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fcG4-_q4PScQ"
      },
      "source": [
        "下载github的文件，并执行"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rUIfVUVUPWAx"
      },
      "source": [
        "!wget https://raw.githubusercontent.com/qiaoyanxie/lyft/main/setup_notebook_colab_1.sh -q\n",
        "!sh /content/setup_notebook_colab_1.sh"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KEaPcixpQ1Xi",
        "outputId": "e19b0a80-fe27-47d5-c794-f1e7bac43115"
      },
      "source": [
        "!echo \"# 111\" >> README.md\n",
        "!git init\n",
        "!git add README.md\n",
        "!git commit -m \"first commit\"\n",
        "!git branch -M main\n",
        "!git remote add origin https://github.com/qiaoyanxie/111.git\n",
        "!git push -u origin main"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Initialized empty Git repository in /content/.git/\n",
            "\n",
            "*** Please tell me who you are.\n",
            "\n",
            "Run\n",
            "\n",
            "  git config --global user.email \"you@example.com\"\n",
            "  git config --global user.name \"Your Name\"\n",
            "\n",
            "to set your account's default identity.\n",
            "Omit --global to set the identity only in this repository.\n",
            "\n",
            "fatal: unable to auto-detect email address (got 'root@add8cb1d0a5e.(none)')\n",
            "error: refname refs/heads/master not found\n",
            "fatal: Branch rename failed\n",
            "error: src refspec main does not match any.\n",
            "error: failed to push some refs to 'https://github.com/qiaoyanxie/111.git'\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3fWo2NJUR2mR",
        "outputId": "809ac13f-1288-47cb-d5b0-d8a82ad8b85d"
      },
      "source": [
        "!git remote add origin https://github.com/qiaoyanxie/111.git\n",
        "!git branch -M main\n",
        "!git push -u origin main"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "fatal: remote origin already exists.\n",
            "error: refname refs/heads/master not found\n",
            "fatal: Branch rename failed\n",
            "error: src refspec main does not match any.\n",
            "error: failed to push some refs to 'https://github.com/qiaoyanxie/111.git'\n"
          ]
        }
      ]
    }
  ]
}