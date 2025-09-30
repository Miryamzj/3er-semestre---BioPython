
SECUENCIA_DNA= "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

CODON_TABLA = {
    "AUG": "Met", "UUU": "Phe", "UUC": "Phe",
    "UUA": "Leu", "UUG": "Leu", "CUU": "Leu", "CUC": "Leu",
    "CUA": "Leu", "CUG": "Leu", "AUU": "Ile", "AUC": "Ile",
    "AUA": "Ile", "GUU": "Val", "GUC": "Val", "GUA": "Val",
    "GUG": "Val", "UCU": "Ser", "UCC": "Ser", "UCA": "Ser",
    "UCG": "Ser", "CCU": "Pro", "CCC": "Pro", "CCA": "Pro",
    "CCG": "Pro", "ACU": "Thr", "ACC": "Thr", "ACA": "Thr",
    "ACG": "Thr", "UAU": "Tyr", "UAC": "Tyr", "CAU": "His",
    "CAC": "His", "CAA": "Gln", "CAG": "Gln", "AAU": "Asn",
    "AAC": "Asn", "AAA": "Lys", "AAG": "Lys", "GAU": "Asp",
    "GAC": "Asp", "GAA": "Glu", "GAG": "Glu", "UGU": "Cys",
    "UGC": "Cys", "UGG": "Trp", "CGU": "Arg", "CGC": "Arg",
    "CGA": "Arg", "AGA": "Arg", "AGG": "Arg", "GGU": "Gly",
    "GGC": "Gly", "GGA": "Gly", "GGG": "Gly", "UAA": "STOP",
    "UAG": "STOP", "UGA": "STOP"
}
START_CODON = "AUG"
STOP_CODONS = {"UAG", "UGA", "UAA"}

def reverse_complement_dna(seq_dna: str) -> str:
    #Devuelve la hebra reverso-complementaria en ADN (A<->T, C<->G, y al revés)
    comp = str.maketrans({"A":"T","T":"A","C":"G","G":"C"})
    return seq_dna.upper().translate(comp)[::-1]

def transcribe_dna_to_rna(seq_dna: str) -> str:
    #Transcripción simple: ADN (hebra codificante) → ARN (T→U)."""
    return seq_dna.upper().replace("T","U")

# === Traducción/ORFs en una hebra de ARN ===
def translate_codon(codon: str) -> str:
    #Traduce un codón (ARN) a 1 letra; 'X' si no mapea."""
    return CODON_TABLA.get(codon, "X")

def scan_orfs_in_rna(rna: str, strand_label: str):
    """
    Escanea los 3 frames de una hebra de ARN:
    - ORF inicia en AUG
    - termina en STOP (no incluye '*') o en fin de cadena
    Devuelve lista de dicts con metadatos.
    """
    resultados = []
    n = len(rna)
    for frame in (0,1,2):
        i = frame
        while i + 3 <= n:
            codon = rna[i:i+3]
            if codon == START_CODON:
                # Abrimos ORF y traducimos hasta STOP o final
                aa = []
                j = i
                while j + 3 <= n:
                    c = rna[j:j+3]
                    if c in STOP_CODONS:
                        break
                    aa.append(translate_codon(c))
                    j += 3
                # Guardamos si tiene longitud >= 1 aa
                if len(aa) > 0:
                    resultados.append({
                        "strand": strand_label,       # '+' o '-'
                        "frame": frame,               # 0,1,2
                        "rna_start": i,               # índice nt en esta hebra de ARN
                        "rna_end_exclusive": j,       # fin exclusivo (hasta antes de STOP o fin)
                        "aa_len": len(aa),
                        "protein": "".join(aa)
                    })
                # Avanzamos 3 nt para permitir ORFs solapados (no saltar hasta j)
                i += 3
            else:
                i += 3
    return resultados

# === Orquestador 6 frames ===
def find_all_orfs_from_dna(seq_dna: str):
    # Hebra +
    rna_plus = transcribe_dna_to_rna(seq_dna)
    orfs_plus = scan_orfs_in_rna(rna_plus, "+")
    # Hebra − (reverso-complementaria → luego transcribir)
    dna_minus = reverse_complement_dna(seq_dna)
    rna_minus = transcribe_dna_to_rna(dna_minus)
    orfs_minus = scan_orfs_in_rna(rna_minus, "-")
    # Unimos y ordenamos por longitud AA desc.
    todos = orfs_plus + orfs_minus
    todos.sort(key=lambda d: d["aa_len"], reverse=True)
    return todos, rna_plus, rna_minus

# === Ejecutar con la secuencia dada ===
if __name__ == "__main__":
    orfs, rna_plus, rna_minus = find_all_orfs_from_dna(SECUENCIA_DNA)

    # Mostrar resumen
    print("ARN (hebra +):", rna_plus)
    print("ARN (hebra INVERSA -):", rna_minus)
    print("\nORFs encontrados (ordenados por longitud):")
    for k, entry in enumerate(orfs, 1):
        print(f"{k:02d}. strand={entry['strand']} frame={entry['frame']} "
              f"rna[{entry['rna_start']}:{entry['rna_end_exclusive']}] "
              f"aa_len={entry['aa_len']}  prot={entry['protein']}")

    # proteína(s) de mayor longitud
    if orfs:
        max_len = orfs[0]["aa_len"]
        mejores = [e for e in orfs if e["aa_len"] == max_len]
        print("\nProteína(s) más larga(s):")
        for e in mejores:
            print(f"- strand={e['strand']} frame={e['frame']} len={e['aa_len']} prot={e['protein']}")
    else:
        print("\nNo se encontraron ORFs.")
