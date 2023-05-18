import kmp_search
import kr_search
import naive_search
import time
import matplotlib.pyplot as plt
import gc


if __name__ == '__main__':
    path = "pan-tadeusz-unix.txt"
    number_of_words = [i for i in range(100, 1001, 100)]
    times_kmp = []
    times_naive = []
    times_kr = []
    q = 101

    with open(path, "r") as file:
        whole_file = file.read()

    for n in number_of_words:
        with open(path, "r") as file:
            first_n_words = file.read().split()[:n]

            # # ----------------------------------------------------------------------
            # #  NAIVE
            # # ----------------------------------------------------------------------

            gc_old = gc.isenabled()
            gc.disable()

            naive_start = time.process_time()

            for i in first_n_words:
                naive_search.find_n(i, whole_file)

            naive_stop = time.process_time()

            if gc_old:
                gc.enable()

            times_naive.append(naive_stop - naive_start)

            print(f"Ukonczono {n} słow w NAIVE")

            # # ----------------------------------------------------------------------
            # #  KMP
            # # ----------------------------------------------------------------------

            gc_old = gc.isenabled()
            gc.disable()

            kmp_start = time.process_time()

            for i in first_n_words:
                kmp_search.find_kmp(i, whole_file)

            kmp_stop = time.process_time()

            if gc_old:
                gc.enable()

            times_kmp.append(kmp_stop - kmp_start)

            print(f"Ukonczono {n} słow w KMP")

            # # ----------------------------------------------------------------------
            # #  KR
            # # ----------------------------------------------------------------------

            gc_old = gc.isenabled()
            gc.disable()

            kr_start = time.process_time()

            for i in first_n_words:
                kr_search.find_kr(i, whole_file, q)

            kr_stop = time.process_time()

            if gc_old:
                gc.enable()

            times_kr.append(kr_stop - kr_start)

            print(f"Ukonczono {n} słow w KR")

        print(f"ZROBIONO {n}")

    plt.plot(times_naive, label="naive")
    plt.plot(times_kmp, label="kmp")
    plt.plot(times_kr, label="kr")
    plt.title('Czas wyszukiwania słów')
    plt.xlabel('Liczba słów')
    plt.ylabel('Czas')
    plt.legend()
    plt.xticks(range(len(number_of_words)), number_of_words)
    plt.savefig('Czas_wyszukiwania.jpg', dpi=100)
    plt.show()



