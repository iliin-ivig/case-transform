from case_transform.case_style import CaseStyle, CaseStyleItem


def transform(
    identifier: str,
    *,
    from_style: CaseStyle | None = None,
    to_style: CaseStyle,
) -> str:
    from_style = CaseStyle.detect(identifier) if from_style is None else from_style

    if from_style is None:
        raise ValueError(f'Identifier "{identifier}" doesnt match any of {CaseStyle}.')

    return to_style(*from_style.split(identifier))
