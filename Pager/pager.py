import sys
from math import inf as infinity

def read_pages_from_file(file_name):
    with open(file_name) as file:
        lines = [int(p) for p in file.readlines()]
        frame_count = lines[0]
        pages = lines[1:]
    return [frame_count, pages]

def first_in_first_out(frame_count, pages):
    pages = pages[:]
    frames = [None]*frame_count
    faults = 0

    while pages:
        page = pages.pop(0)

        if page in frames:
            continue
        else:
            faults += 1
            index = (index+1) % frame_count \
                    if all([f is not None for f in frames]) \
                    else frames.index(None)
            frames[index] = page

    return faults

def optimal_page_replacement(frame_count, pages):
    pages = pages[:]
    frames = [None]*frame_count
    faults = 0

    while pages:
        page = pages.pop(0)

        if page in frames:
            continue
        else:
            faults += 1
            if(all([f is not None for f in frames])):
                lengths = {x: pages.index(x) if x in pages else infinity for x in frames}
                index = frames.index(max(lengths, key=lengths.get))
            else:
                index = frames.index(None)
            
            frames[index] = page

    return faults

def least_recently_used(frame_count, pages):
    pages = pages[:]
    used = []
    frames = [None]*frame_count
    faults = 0

    while pages:
        page = pages.pop(0)
        if page in used: used.remove(page)
        used.append(page)

        if page in frames:
            continue
        else:
            faults += 1
            if(all([f is not None for f in frames])):
                lengths = {x: used.index(x) for x in frames}
                index = frames.index(min(lengths, key=lengths.get))
            else:
                index = frames.index(None)
                
            frames[index] = page

    return faults

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python pager.py <pages_file>.txt')
        exit(1)

    frame_count, pages = read_pages_from_file(sys.argv[1])
    print('FIFO {}'.format(first_in_first_out(frame_count, pages)))
    print('OTM {}'.format(optimal_page_replacement(frame_count, pages)))
    print('LRU {}'.format(least_recently_used(frame_count, pages)))