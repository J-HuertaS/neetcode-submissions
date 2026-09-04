class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        options = {}
        l = 0
        r = 0
        current_longest = ''
        longest_len = 0
        output = 0
        while(r < len(s)):
            ch = s[r]
            # actualiza options con el nuevo valor
            options[ch] = options.get(ch,0) + 1

            if options[ch] > longest_len:
                longest_len = options[ch]
                current_longest = ch
                

            # si ya nos pasamos de la cantidad de reemplazos, tenemos que actualizar
            while (r-l+1) - longest_len > k:
                temp = s[l]
                options[temp] -= 1
                if temp == current_longest:
                    # verificar quien es el nuevo longest del options
                    for x,lon in options.items():
                        if lon > longest_len:
                            longest_len = lon
                            current_longest = x
                l += 1
                
            
            # volvemos a un estado de aceptacion
            output = max(output,r-l+1)

            r += 1

        return output

        