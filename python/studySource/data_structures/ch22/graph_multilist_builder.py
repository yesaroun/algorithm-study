from node_edge import NodeEdge

class GraphMultilistBuilder:
    @staticmethod
    def build(mat):
        if not mat:
            raise Exception("the mat should not be none.")

        size = len(mat)
        # test
        # print("size:", size)
        print("mat: ", mat)

        ret = [None] * size
        for row in range(size):
            for col in range(size):
                if not mat[row][col]:
                    print("row:", row)
                    print("col:", col)
                    continue

                if col <= row:
                    continue

                node = NodeEdge(v1=row, v2=col)
                node.link_v1 = ret[row]
                node.link_v2 = ret[col]
                print("ret[]", ret)
                ret[row] = node
                ret[col] = node

        return ret