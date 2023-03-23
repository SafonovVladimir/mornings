def triangle(row: str) -> str:
    while len(row) > 1:
        result = []
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                result.append(row[i])
            else:
                result.append(
                    "RGB".replace(row[i], "").replace(row[i + 1], "")
                )
        row = result

    return "".join(row)


print(triangle("RRGBRGBB"))